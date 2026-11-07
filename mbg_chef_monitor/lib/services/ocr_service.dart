import 'dart:math';
import 'package:google_mlkit_text_recognition/google_mlkit_text_recognition.dart';

class OcrResult {
  final double weight;
  final double confidence;
  final String rawText;
  final List<double> alternatives;
  final String? detectedUnit;

  const OcrResult({
    required this.weight,
    required this.confidence,
    required this.rawText,
    this.alternatives = const [],
    this.detectedUnit,
  });
}

class OcrService {
  final TextRecognizer _recognizer =
      TextRecognizer(script: TextRecognitionScript.latin);

  // Status kata-kata pada timbangan digital yang sering muncul di sekitar angka
  static const Set<String> _scaleKeywords = {
    'NET', 'GROSS', 'TARE', 'STABLE', 'ZERO', 'HOLD', 'PCS', 'CAP',
    'MAX', 'MIN', 'W1', 'W2', 'CAL', 'TOTAL', 'BATERAI', 'LOW'
  };

  /// Ekstraksi berat dengan tuning khusus display 7-Segment LED / LCD
  Future<OcrResult?> extractWeightFromImage(String imagePath) async {
    try {
      final inputImage = InputImage.fromFilePath(imagePath);
      final RecognizedText recognized = await _recognizer.processImage(inputImage);

      final List<_Candidate> candidates = [];

      for (final TextBlock block in recognized.blocks) {
        for (final TextLine line in block.lines) {
          final String rawLine = line.text;
          final List<_Candidate> lineCandidates = _parseLineCandidates(rawLine);
          candidates.addAll(lineCandidates);
        }
      }

      if (candidates.isEmpty) {
        // Fallback: proses full text secara keseluruhan jika line-by-line gagal
        final String fullText = recognized.text;
        final List<_Candidate> fullTextCandidates = _parseLineCandidates(fullText);
        candidates.addAll(fullTextCandidates);
      }

      if (candidates.isEmpty) return null;

      // Urutkan candidate berdasarkan skor confidence tertinggi
      candidates.sort((a, b) => b.score.compareTo(a.score));

      final _Candidate best = candidates.first;
      final List<double> altList = candidates
          .skip(1)
          .map((c) => c.weight)
          .where((w) => (w - best.weight).abs() > 0.009)
          .toSet()
          .take(3)
          .toList();

      return OcrResult(
        weight: best.weight,
        confidence: best.score,
        rawText: best.rawToken,
        alternatives: altList,
        detectedUnit: best.unit,
      );
    } catch (e) {
      return null;
    }
  }

  /// Parser kandidat angka dari satu baris teks OCR
  List<_Candidate> _parseLineCandidates(String text) {
    final List<_Candidate> results = [];
    if (text.trim().isEmpty) return results;

    final String upper = text.toUpperCase();

    // Deteksi indikasi unit (kg vs gram)
    bool hasKg = upper.contains('KG') || upper.contains('KGS');
    bool hasGram = !hasKg && (upper.contains(' G ') || upper.endsWith(' G') || upper.contains('GRAM'));

    // Langkah 1: Normalisasi karakter khas 7-segment digital LED
    final String normalized = _normalizeLedCharacters(upper);

    // Langkah 2: Evaluasi Pola Regex
    // Pola A: Angka desimal 2 digit di belakang koma (Paling umum di timbangan MBG: 12.50, 1.75, 73.16)
    final RegExp decimal2Regex = RegExp(r'(?:^|[^\d])(\d{1,3}[\.,:]\d{2})(?:[^\d]|$)');
    for (final Match m in decimal2Regex.allMatches(normalized)) {
      final String rawMatch = m.group(1)!;
      final double? parsed = _parseNumericValue(rawMatch, hasGram);
      if (parsed != null && _isValidKitchenWeight(parsed)) {
        double score = 0.95;
        if (hasKg) score += 0.05;
        results.add(_Candidate(weight: parsed, score: min(1.0, score), rawToken: rawMatch, unit: hasGram ? 'g' : 'kg'));
      }
    }

    // Pola B: Angka desimal 3 digit di belakang koma (Timbangan presisi: 1.250, 0.450)
    final RegExp decimal3Regex = RegExp(r'(?:^|[^\d])(\d{1,3}[\.,:]\d{3})(?:[^\d]|$)');
    for (final Match m in decimal3Regex.allMatches(normalized)) {
      final String rawMatch = m.group(1)!;
      final double? parsed = _parseNumericValue(rawMatch, hasGram);
      if (parsed != null && _isValidKitchenWeight(parsed)) {
        double score = 0.90;
        if (hasKg) score += 0.08;
        results.add(_Candidate(weight: parsed, score: min(1.0, score), rawToken: rawMatch, unit: hasGram ? 'g' : 'kg'));
      }
    }

    // Pola C: Angka desimal 1 digit di belakang koma (contoh: 15.5 kg)
    final RegExp decimal1Regex = RegExp(r'(?:^|[^\d])(\d{1,3}[\.,:]\d{1})(?:[^\d]|$)');
    for (final Match m in decimal1Regex.allMatches(normalized)) {
      final String rawMatch = m.group(1)!;
      final double? parsed = _parseNumericValue(rawMatch, hasGram);
      if (parsed != null && _isValidKitchenWeight(parsed)) {
        results.add(_Candidate(weight: parsed, score: 0.80, rawToken: rawMatch, unit: hasGram ? 'g' : 'kg'));
      }
    }

    // Pola D: Angka bulat utuh (contoh: 25 kg, atau timbangan yang titik desimal LED-nya terputus/buram)
    // Timbangan digital seringkali titik LED-nya tidak terbaca sehingga 15.80 terbaca 1580
    final RegExp integerRegex = RegExp(r'(?:^|[^\d])(\d{2,5})(?:[^\d]|$)');
    for (final Match m in integerRegex.allMatches(normalized)) {
      final String rawMatch = m.group(1)!;
      final double? intVal = double.tryParse(rawMatch);
      if (intVal != null) {
        // Kasus D.1: Angka bulat valid 1 - 150 kg
        if (intVal >= 1.0 && intVal <= 150.0) {
          results.add(_Candidate(weight: intVal, score: 0.70, rawToken: rawMatch, unit: 'kg'));
        }
        // Kasus D.2: Rekonstruksi titik desimal yang hilang dari LED 7-segment (contoh: 1250 -> 12.50)
        if (rawMatch.length == 4 || rawMatch.length == 3) {
          final double restored = intVal / 100.0;
          if (_isValidKitchenWeight(restored)) {
            results.add(_Candidate(weight: restored, score: 0.65, rawToken: '$rawMatch (auto .)', unit: 'kg'));
          }
        }
      }
    }

    return results;
  }

  /// Pembersihan & pemulihan karakter 7-segment LED
  /// Seringkali segmen LED yang putus terbaca huruf alfanumerik oleh model OCR umum
  String _normalizeLedCharacters(String input) {
    String clean = input;

    // Bersihkan keyword timbangan terlebih dahulu agar tidak salah di-replace
    for (final kw in _scaleKeywords) {
      clean = clean.replaceAll(kw, ' ');
    }

    // Bersihkan spasi di antara digit dan titik/koma (e.g. "12 . 50" -> "12.50")
    clean = clean.replaceAllMapped(RegExp(r'(\d)\s*[\.,:]\s*(\d)'), (m) => '${m[1]}.${m[2]}');

    final StringBuffer sb = StringBuffer();
    for (int i = 0; i < clean.length; i++) {
      final char = clean[i];
      // Substitusi huruf ke angka jika berada dalam konteks numerik LED
      switch (char) {
        case 'S':
        case 's':
          sb.write('5');
          break;
        case 'O':
        case 'o':
        case 'D':
        case 'Q':
          sb.write('0');
          break;
        case 'I':
        case 'l':
        case '|':
        case '!':
        case '/':
        case ']':
        case '[':
          sb.write('1');
          break;
        case 'B':
          sb.write('8');
          break;
        case 'Z':
        case 'z':
          sb.write('2');
          break;
        case 'A':
          sb.write('4');
          break;
        case 'T':
          sb.write('7');
          break;
        case 'G':
        case 'b':
          sb.write('6');
          break;
        case ',':
        case ':':
        case ';':
          sb.write('.');
          break;
        default:
          sb.write(char);
      }
    }
    return sb.toString();
  }

  double? _parseNumericValue(String raw, bool isGram) {
    final String sanitized = raw.replaceAll(',', '.').replaceAll(':', '.');
    final double? val = double.tryParse(sanitized);
    if (val == null) return null;

    if (isGram) {
      // Konversi gram ke kg untuk konsistensi dapur MBG
      return val / 1000.0;
    }
    return val;
  }

  /// Validasi batas berat dapur MBG (0.05 kg s/d 200 kg per wadah timbangan)
  bool _isValidKitchenWeight(double weight) {
    return weight >= 0.05 && weight <= 250.0;
  }

  void dispose() {
    _recognizer.close();
  }
}

class _Candidate {
  final double weight;
  final double score;
  final String rawToken;
  final String unit;

  _Candidate({
    required this.weight,
    required this.score,
    required this.rawToken,
    required this.unit,
  });
}

