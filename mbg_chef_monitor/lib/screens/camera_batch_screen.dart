import 'dart:io';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import '../models/weigh_batch.dart';
import '../services/ocr_service.dart';
import 'review_sync_screen.dart';

class CameraBatchScreen extends StatefulWidget {
  final String tanggal;
  final String kategori;
  final String tahapan;
  final String itemMenu;
  final String petugas;
  final double defaultTarePerBatch;
  final String? initialImagePath;

  const CameraBatchScreen({
    super.key,
    required this.tanggal,
    required this.kategori,
    required this.tahapan,
    required this.itemMenu,
    required this.petugas,
    required this.defaultTarePerBatch,
    this.initialImagePath,
  });

  @override
  State<CameraBatchScreen> createState() => _CameraBatchScreenState();
}

class _CameraBatchScreenState extends State<CameraBatchScreen> {
  final ImagePicker _picker = ImagePicker();
  final OcrService _ocrService = OcrService();
  final List<WeighBatchItem> _batchItems = [];

  bool _isProcessingOcr = false;
  late double _activeTare;

  @override
  void initState() {
    super.initState();
    _activeTare = widget.defaultTarePerBatch;

    // Jika ada foto yang sudah dipilih dari galeri di halaman awal
    if (widget.initialImagePath != null && widget.initialImagePath!.isNotEmpty) {
      WidgetsBinding.instance.addPostFrameCallback((_) {
        _processImage(widget.initialImagePath!);
      });
    }
  }

  @override
  void dispose() {
    _ocrService.dispose();
    super.dispose();
  }

  double get _totalGross =>
      _batchItems.fold(0.0, (sum, item) => sum + item.grossWeight);

  double get _totalTare =>
      _batchItems.fold(0.0, (sum, item) => sum + item.tareWeight);

  double get _totalNet =>
      _batchItems.fold(0.0, (sum, item) => sum + item.netWeight);

  Future<void> _pickImage(ImageSource source) async {
    try {
      final XFile? photo = await _picker.pickImage(
        source: source,
        imageQuality: 92,
      );

      if (photo == null) return;
      await _processImage(photo.path);
    } catch (e) {
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text("Gagal mengambil gambar: $e"),
            behavior: SnackBarBehavior.floating,
          ),
        );
      }
    }
  }

  Future<void> _processImage(String path) async {
    setState(() => _isProcessingOcr = true);
    final OcrResult? result = await _ocrService.extractWeightFromImage(path);
    setState(() => _isProcessingOcr = false);

    if (!mounted) return;

    if (result != null) {
      _showDetectedWeightConfirmation(
        grossWeight: result.weight,
        imagePath: path,
        confidence: result.confidence,
        alternatives: result.alternatives,
        rawText: result.rawText,
      );
    } else {
      _showManualInputDialog(
        imagePath: path,
        titleText: "Angka LED Belum Terdeteksi",
        subtitleText: "Display silau atau buram. Masukkan berat secara manual:",
      );
    }
  }

  void _showDetectedWeightConfirmation({
    required double grossWeight,
    required String imagePath,
    required double confidence,
    required List<double> alternatives,
    required String rawText,
  }) {
    double currentVal = grossWeight;
    final textController = TextEditingController(text: currentVal.toStringAsFixed(2));

    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.white,
      shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(24)),
      ),
      builder: (ctx) {
        return StatefulBuilder(
          builder: (context, setModalState) {
            final double netVal = (currentVal - _activeTare) > 0 ? (currentVal - _activeTare) : 0.0;
            return Padding(
              padding: EdgeInsets.only(
                left: 24,
                right: 24,
                top: 24,
                bottom: MediaQuery.of(ctx).viewInsets.bottom + 24,
              ),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text(
                        "Wadah ke-${_batchItems.length + 1}",
                        style: const TextStyle(
                          fontSize: 18,
                          fontWeight: FontWeight.w700,
                          color: Color(0xFF0F172A),
                        ),
                      ),
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                        decoration: BoxDecoration(
                          color: confidence > 0.85
                              ? const Color(0xFFECFDF5)
                              : const Color(0xFFFFFBEB),
                          borderRadius: BorderRadius.circular(20),
                          border: Border.all(
                            color: confidence > 0.85
                                ? const Color(0xFFA7F3D0)
                                : const Color(0xFFFDE68A),
                          ),
                        ),
                        child: Text(
                          "Akurasi: ${(confidence * 100).toInt()}%",
                          style: TextStyle(
                            fontSize: 12,
                            fontWeight: FontWeight.w600,
                            color: confidence > 0.85
                                ? const Color(0xFF065F46)
                                : const Color(0xFF92400E),
                          ),
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 16),
                  Row(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      ClipRRect(
                        borderRadius: BorderRadius.circular(12),
                        child: Image.file(
                          File(imagePath),
                          width: 90,
                          height: 90,
                          fit: BoxFit.cover,
                        ),
                      ),
                      const SizedBox(width: 16),
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            const Text(
                              "Berat Terbaca (Bruto):",
                              style: TextStyle(fontSize: 12, color: Color(0xFF64748B)),
                            ),
                            TextField(
                              controller: textController,
                              keyboardType: const TextInputType.numberWithOptions(decimal: true),
                              style: const TextStyle(
                                fontSize: 26,
                                fontWeight: FontWeight.w700,
                                color: Color(0xFF0F172A),
                              ),
                              decoration: const InputDecoration(
                                suffixText: "kg",
                                suffixStyle: TextStyle(
                                  fontSize: 16,
                                  fontWeight: FontWeight.w600,
                                  color: Color(0xFF059669),
                                ),
                                contentPadding: EdgeInsets.symmetric(horizontal: 12, vertical: 8),
                              ),
                              onChanged: (val) {
                                final p = double.tryParse(val.replaceAll(',', '.'));
                                if (p != null) {
                                  setModalState(() => currentVal = p);
                                }
                              },
                            ),
                            const SizedBox(height: 6),
                            Text(
                              "Tara: ${_activeTare.toStringAsFixed(2)} kg  •  Netto: ${netVal.toStringAsFixed(2)} kg",
                              style: const TextStyle(
                                fontSize: 13,
                                fontWeight: FontWeight.w600,
                                color: Color(0xFF059669),
                              ),
                            ),
                          ],
                        ),
                      ),
                    ],
                  ),
                  if (alternatives.isNotEmpty) ...[
                    const SizedBox(height: 14),
                    const Text(
                      "Pilihan Angka Lain:",
                      style: TextStyle(fontSize: 12, color: Color(0xFF64748B)),
                    ),
                    const SizedBox(height: 6),
                    Wrap(
                      spacing: 8,
                      children: alternatives.map((alt) {
                        return ActionChip(
                          backgroundColor: const Color(0xFFF1F5F9),
                          side: const BorderSide(color: Color(0xFFCBD5E1)),
                          label: Text(
                            "${alt.toStringAsFixed(2)} kg",
                            style: const TextStyle(fontSize: 12, fontWeight: FontWeight.w600),
                          ),
                          onPressed: () {
                            setModalState(() {
                              currentVal = alt;
                              textController.text = alt.toStringAsFixed(2);
                            });
                          },
                        );
                      }).toList(),
                    ),
                  ],
                  const SizedBox(height: 20),
                  SizedBox(
                    width: double.infinity,
                    height: 48,
                    child: ElevatedButton(
                      style: ElevatedButton.styleFrom(
                        backgroundColor: const Color(0xFF0F172A),
                        foregroundColor: Colors.white,
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                      ),
                      onPressed: () {
                        final finalVal =
                            double.tryParse(textController.text.replaceAll(',', '.')) ?? currentVal;
                        setState(() {
                          _batchItems.add(
                            WeighBatchItem(
                              id: DateTime.now().millisecondsSinceEpoch.toString(),
                              grossWeight: finalVal,
                              tareWeight: _activeTare,
                              imagePath: imagePath,
                              rawOcrConfidence: confidence,
                            ),
                          );
                        });
                        Navigator.pop(ctx);
                      },
                      child: const Text("Simpan Wadah Ini", style: TextStyle(fontWeight: FontWeight.w600)),
                    ),
                  ),
                ],
              ),
            );
          },
        );
      },
    );
  }

  void _showManualInputDialog({
    String? imagePath,
    String titleText = "Input Berat Manual",
    String subtitleText = "Masukkan berat bruto timbangan (kg):",
  }) {
    final textController = TextEditingController();
    showDialog(
      context: context,
      builder: (ctx) {
        return AlertDialog(
          backgroundColor: Colors.white,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(18)),
          title: Text(
            titleText,
            style: const TextStyle(fontSize: 18, fontWeight: FontWeight.w700),
          ),
          content: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                subtitleText,
                style: const TextStyle(fontSize: 13, color: Color(0xFF64748B)),
              ),
              const SizedBox(height: 14),
              TextField(
                controller: textController,
                autofocus: true,
                keyboardType: const TextInputType.numberWithOptions(decimal: true),
                style: const TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
                decoration: const InputDecoration(
                  hintText: "Contoh: 12.50",
                  suffixText: "kg",
                ),
              ),
              const SizedBox(height: 10),
              Text(
                "Tara aktif: ${_activeTare.toStringAsFixed(2)} kg",
                style: const TextStyle(fontSize: 12, color: Color(0xFF64748B)),
              ),
            ],
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.pop(ctx),
              child: const Text("Batal", style: TextStyle(color: Color(0xFF64748B))),
            ),
            ElevatedButton(
              style: ElevatedButton.styleFrom(
                backgroundColor: const Color(0xFF0F172A),
                foregroundColor: Colors.white,
              ),
              onPressed: () {
                final val = double.tryParse(textController.text.replaceAll(',', '.'));
                if (val != null && val > 0) {
                  setState(() {
                    _batchItems.add(
                      WeighBatchItem(
                        id: DateTime.now().millisecondsSinceEpoch.toString(),
                        grossWeight: val,
                        tareWeight: _activeTare,
                        imagePath: imagePath ?? '',
                        isManual: true,
                      ),
                    );
                  });
                  Navigator.pop(ctx);
                }
              },
              child: const Text("Simpan"),
            ),
          ],
        );
      },
    );
  }

  void _editBatchItem(int index) {
    final item = _batchItems[index];
    final textController = TextEditingController(text: item.grossWeight.toStringAsFixed(2));

    showDialog(
      context: context,
      builder: (ctx) {
        return AlertDialog(
          backgroundColor: Colors.white,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(18)),
          title: Text("Ubah Wadah ke-${index + 1}"),
          content: TextField(
            controller: textController,
            keyboardType: const TextInputType.numberWithOptions(decimal: true),
            style: const TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
            decoration: const InputDecoration(suffixText: "kg"),
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.pop(ctx),
              child: const Text("Batal", style: TextStyle(color: Color(0xFF64748B))),
            ),
            ElevatedButton(
              onPressed: () {
                final val = double.tryParse(textController.text.replaceAll(',', '.'));
                if (val != null && val > 0) {
                  setState(() {
                    _batchItems[index] = WeighBatchItem(
                      id: item.id,
                      grossWeight: val,
                      tareWeight: item.tareWeight,
                      imagePath: item.imagePath,
                      isManual: true,
                    );
                  });
                  Navigator.pop(ctx);
                }
              },
              child: const Text("Perbarui"),
            ),
          ],
        );
      },
    );
  }

  void _proceedToReview() {
    if (_batchItems.isEmpty) return;

    final session = WeighSession(
      id: DateTime.now().millisecondsSinceEpoch.toString(),
      tanggal: widget.tanggal,
      waktu: TimeOfDay.now().format(context),
      timKerja: widget.tahapan,
      itemMenu: widget.itemMenu,
      kategori: widget.kategori,
      tahapan: widget.tahapan,
      defaultTarePerContainer: _activeTare,
      batches: _batchItems,
      petugas: widget.petugas,
    );

    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (_) => ReviewSyncScreen(session: session),
      ),
    ).then((result) {
      if (result == true && mounted) {
        Navigator.pop(context, session);
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFF8FAFC),
      appBar: AppBar(
        title: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              widget.itemMenu,
              style: const TextStyle(fontSize: 17, fontWeight: FontWeight.w700, color: Color(0xFF0F172A)),
            ),
            Text(
              "${widget.tahapan} • ${widget.kategori}",
              style: const TextStyle(fontSize: 12, color: Color(0xFF64748B), fontWeight: FontWeight.w500),
            ),
          ],
        ),
      ),
      body: Column(
        children: [
          // TOTAL ACCUMULATOR DISPLAY BANNER (MODERN MINIMALIST)
          Container(
            margin: const EdgeInsets.all(16),
            padding: const EdgeInsets.all(20),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(20),
              border: Border.all(color: const Color(0xFFE2E8F0)),
              boxShadow: [
                BoxShadow(
                  color: const Color(0xFF0F172A).withOpacity(0.04),
                  blurRadius: 12,
                  offset: const Offset(0, 4),
                ),
              ],
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    const Text(
                      "TOTAL BERAT NETTO",
                      style: TextStyle(
                        fontSize: 11,
                        fontWeight: FontWeight.w700,
                        letterSpacing: 1.2,
                        color: Color(0xFF64748B),
                      ),
                    ),
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                      decoration: BoxDecoration(
                        color: const Color(0xFFF1F5F9),
                        borderRadius: BorderRadius.circular(20),
                      ),
                      child: Text(
                        "${_batchItems.length} Wadah",
                        style: const TextStyle(
                          fontSize: 12,
                          fontWeight: FontWeight.w700,
                          color: Color(0xFF0F172A),
                        ),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 8),
                Row(
                  crossAxisAlignment: CrossAxisAlignment.baseline,
                  textBaseline: TextBaseline.alphabetic,
                  children: [
                    Text(
                      _totalNet.toStringAsFixed(2),
                      style: const TextStyle(
                        fontSize: 42,
                        fontWeight: FontWeight.w800,
                        color: Color(0xFF0F172A),
                        letterSpacing: -1,
                      ),
                    ),
                    const SizedBox(width: 8),
                    const Text(
                      "kg",
                      style: TextStyle(
                        fontSize: 20,
                        fontWeight: FontWeight.w600,
                        color: Color(0xFF059669),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 12),
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
                  decoration: BoxDecoration(
                    color: const Color(0xFFF8FAFC),
                    borderRadius: BorderRadius.circular(12),
                  ),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text(
                        "Bruto: ${_totalGross.toStringAsFixed(2)} kg",
                        style: const TextStyle(fontSize: 12, color: Color(0xFF64748B), fontWeight: FontWeight.w500),
                      ),
                      Text(
                        "Tara: ${_totalTare.toStringAsFixed(2)} kg",
                        style: const TextStyle(fontSize: 12, color: Color(0xFF64748B), fontWeight: FontWeight.w500),
                      ),
                      Text(
                        "Tara/Wadah: ${_activeTare.toStringAsFixed(2)} kg",
                        style: const TextStyle(fontSize: 12, color: Color(0xFF059669), fontWeight: FontWeight.w600),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),

          // LIST WADAH YANG TERTIMBANG
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 20),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                const Text(
                  "Rincian Wadah",
                  style: TextStyle(fontSize: 14, fontWeight: FontWeight.w700, color: Color(0xFF0F172A)),
                ),
                if (_batchItems.isNotEmpty)
                  TextButton(
                    onPressed: () => setState(() => _batchItems.clear()),
                    child: const Text("Reset", style: TextStyle(color: Color(0xFFDC2626), fontSize: 13)),
                  ),
              ],
            ),
          ),

          Expanded(
            child: _batchItems.isEmpty
                ? Center(
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Icon(Icons.scale_outlined, size: 52, color: Colors.grey.shade400),
                        const SizedBox(height: 12),
                        const Text(
                          "Belum ada wadah ditimbang",
                          style: TextStyle(fontSize: 15, fontWeight: FontWeight.w600, color: Color(0xFF64748B)),
                        ),
                        const SizedBox(height: 4),
                        const Text(
                          "Gunakan kamera langsung atau ambil foto dari galeri",
                          style: TextStyle(fontSize: 12, color: Color(0xFF94A3B8)),
                        ),
                      ],
                    ),
                  )
                : ListView.builder(
                    padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                    itemCount: _batchItems.length,
                    itemBuilder: (context, idx) {
                      final item = _batchItems[idx];
                      return Container(
                        margin: const EdgeInsets.only(bottom: 10),
                        padding: const EdgeInsets.all(12),
                        decoration: BoxDecoration(
                          color: Colors.white,
                          borderRadius: BorderRadius.circular(14),
                          border: Border.all(color: const Color(0xFFE2E8F0)),
                        ),
                        child: Row(
                          children: [
                            if (item.imagePath != null && item.imagePath!.isNotEmpty && File(item.imagePath!).existsSync())
                              ClipRRect(
                                borderRadius: BorderRadius.circular(8),
                                child: Image.file(
                                  File(item.imagePath!),
                                  width: 48,
                                  height: 48,
                                  fit: BoxFit.cover,
                                ),
                              )
                            else
                              Container(
                                width: 48,
                                height: 48,
                                decoration: BoxDecoration(
                                  color: const Color(0xFFF1F5F9),
                                  borderRadius: BorderRadius.circular(8),
                                ),
                                child: const Icon(Icons.scale, color: Color(0xFF64748B)),
                              ),
                            const SizedBox(width: 12),
                            Expanded(
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Text(
                                    "Wadah #${idx + 1} — ${item.netWeight.toStringAsFixed(2)} kg",
                                    style: const TextStyle(fontWeight: FontWeight.w700, fontSize: 14),
                                  ),
                                  const SizedBox(height: 2),
                                  Text(
                                    "Bruto: ${item.grossWeight.toStringAsFixed(2)} kg • Tara: ${item.tareWeight.toStringAsFixed(2)} kg",
                                    style: const TextStyle(fontSize: 12, color: Color(0xFF64748B)),
                                  ),
                                ],
                              ),
                            ),
                            IconButton(
                              icon: const Icon(Icons.edit_outlined, size: 18, color: Color(0xFF64748B)),
                              onPressed: () => _editBatchItem(idx),
                            ),
                            IconButton(
                              icon: const Icon(Icons.close, size: 18, color: Color(0xFFEF4444)),
                              onPressed: () => setState(() => _batchItems.removeAt(idx)),
                            ),
                          ],
                        ),
                      );
                    },
                  ),
          ),

          // MODERN MINIMALIST ACTION BAR
          Container(
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: Colors.white,
              border: const Border(top: BorderSide(color: Color(0xFFE2E8F0))),
              boxShadow: [
                BoxShadow(
                  color: Colors.black.withOpacity(0.03),
                  blurRadius: 10,
                  offset: const Offset(0, -4),
                ),
              ],
            ),
            child: SafeArea(
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Row(
                    children: [
                      // TOMBOL FOTO KAMERA LANGSUNG
                      Expanded(
                        flex: 3,
                        child: ElevatedButton.icon(
                          style: ElevatedButton.styleFrom(
                            backgroundColor: const Color(0xFF0F172A),
                            foregroundColor: Colors.white,
                            padding: const EdgeInsets.symmetric(vertical: 14),
                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                          ),
                          onPressed: _isProcessingOcr ? null : () => _pickImage(ImageSource.camera),
                          icon: _isProcessingOcr
                              ? const SizedBox(
                                  width: 16,
                                  height: 16,
                                  child: CircularProgressIndicator(strokeWidth: 2, color: Colors.white),
                                )
                              : const Icon(Icons.camera_alt_outlined, size: 18),
                          label: Text(
                            _isProcessingOcr ? "Membaca..." : "Kamera",
                            style: const TextStyle(fontSize: 14, fontWeight: FontWeight.w600),
                          ),
                        ),
                      ),
                      const SizedBox(width: 10),

                      // TOMBOL AMBIL DARI GALERI HP
                      Expanded(
                        flex: 3,
                        child: OutlinedButton.icon(
                          style: OutlinedButton.styleFrom(
                            backgroundColor: Colors.white,
                            foregroundColor: const Color(0xFF0F172A),
                            side: const BorderSide(color: Color(0xFFCBD5E1), width: 1.2),
                            padding: const EdgeInsets.symmetric(vertical: 14),
                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                          ),
                          onPressed: _isProcessingOcr ? null : () => _pickImage(ImageSource.gallery),
                          icon: const Icon(Icons.photo_library_outlined, size: 18),
                          label: const Text(
                            "Galeri",
                            style: TextStyle(fontSize: 14, fontWeight: FontWeight.w600),
                          ),
                        ),
                      ),
                      const SizedBox(width: 8),

                      // TOMBOL MANUAL INPUT
                      IconButton(
                        style: IconButton.styleFrom(
                          backgroundColor: const Color(0xFFF1F5F9),
                          padding: const EdgeInsets.all(12),
                          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                        ),
                        icon: const Icon(Icons.keyboard_alt_outlined, size: 20, color: Color(0xFF334155)),
                        tooltip: "Input Manual",
                        onPressed: () => _showManualInputDialog(),
                      ),
                    ],
                  ),
                  const SizedBox(height: 10),

                  // TOMBOL SELESAI / REVIEW BATCH
                  SizedBox(
                    width: double.infinity,
                    child: ElevatedButton(
                      style: ElevatedButton.styleFrom(
                        backgroundColor: _batchItems.isEmpty ? const Color(0xFF94A3B8) : const Color(0xFF059669),
                        foregroundColor: Colors.white,
                        padding: const EdgeInsets.symmetric(vertical: 14),
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                      ),
                      onPressed: _batchItems.isEmpty ? null : _proceedToReview,
                      child: Text(
                        _batchItems.isEmpty
                            ? "Selesaikan Sesi (Timbang Dulu)"
                            : "Selesai (${_batchItems.length} Wadah • ${_totalNet.toStringAsFixed(2)} kg)",
                        style: const TextStyle(fontSize: 15, fontWeight: FontWeight.w700),
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}
