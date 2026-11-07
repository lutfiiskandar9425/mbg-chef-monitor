import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';
import '../models/weigh_batch.dart';

class SheetsSyncResult {
  final bool isSuccess;
  final String message;
  final int statusCode;

  const SheetsSyncResult({
    required this.isSuccess,
    required this.message,
    this.statusCode = 0,
  });
}

class SheetsService {
  static const String _prefKeyWebhookUrl = "mbg_sheets_webhook_url";
  static const String _defaultUrl =
      "https://script.google.com/macros/s/AKfycby08_sY6VmSOS1WbUFpNIDEUS9NthbaTMaeaYYzJuoxaHKAAJUSOieBBlyfYBnBaL2D/exec";

  static Future<String> getWebhookUrl() async {
    final prefs = await SharedPreferences.getInstance();
    final saved = prefs.getString(_prefKeyWebhookUrl);
    if (saved != null && saved.trim().isNotEmpty) {
      return saved.trim();
    }
    return _defaultUrl;
  }

  static Future<void> saveWebhookUrl(String url) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString(_prefKeyWebhookUrl, url.trim());
  }

  /// Kirim satu sesi timbangan tunggal
  static Future<SheetsSyncResult> syncWeighSession(WeighSession session) async {
    return _sendPayload(session.toWebhookPayload());
  }

  /// Kirim seluruh keranjang berkas TIM (Tim Persiapan, Tim Pengolahan Prohe/Prona/Sayur, Tim Pemorsian)
  static Future<SheetsSyncResult> syncTeamBatch(TeamBatchStaging batch) async {
    return _sendPayload(batch.toBatchWebhookPayload());
  }

  static Future<SheetsSyncResult> _sendPayload(Map<String, dynamic> payload) async {
    final String targetUrl = await getWebhookUrl();

    if (targetUrl.contains("YOUR_SCRIPT_ID_HERE") || !targetUrl.startsWith("http")) {
      return const SheetsSyncResult(
        isSuccess: false,
        message: "URL Webhook Google Sheets belum dikonfigurasi.",
      );
    }

    try {
      final uri = Uri.parse(targetUrl);
      final client = http.Client();
      try {
        final request = http.Request('POST', uri)
          ..headers['Content-Type'] = 'application/json'
          ..headers['Accept'] = 'application/json'
          ..body = jsonEncode(payload);

        final streamedResponse = await client.send(request).timeout(
          const Duration(seconds: 15),
        );
        final response = await http.Response.fromStream(streamedResponse);

        if (response.statusCode == 200 || response.statusCode == 302) {
          return const SheetsSyncResult(
            isSuccess: true,
            message: "Batch timbangan tim berhasil diverifikasi & dicatat ke Google Sheets.",
            statusCode: 200,
          );
        } else {
          return SheetsSyncResult(
            isSuccess: false,
            message: "Server merespons kode HTTP ${response.statusCode}: ${response.reasonPhrase}",
            statusCode: response.statusCode,
          );
        }
      } finally {
        client.close();
      }
    } catch (e) {
      return SheetsSyncResult(
        isSuccess: false,
        message: "Koneksi gagal: pastikan HP terhubung ke internet. ($e)",
      );
    }
  }

  static Future<List<WarehouseStockItem>> fetchWarehouseStock() async {
    final String targetUrl = await getWebhookUrl();
    if (targetUrl.contains("YOUR_SCRIPT_ID_HERE") || !targetUrl.startsWith("http")) {
      return [];
    }

    try {
      final uri = Uri.parse(targetUrl);
      final response = await http.get(uri).timeout(const Duration(seconds: 10));

      if (response.statusCode == 200) {
        final Map<String, dynamic> body = jsonDecode(response.body);
        if (body['status'] == 'success' && body['data'] is List) {
          final List list = body['data'];
          return list.map((item) => WarehouseStockItem.fromJson(item)).toList();
        }
      }
    } catch (_) {}
    return [];
  }

  static Future<void> saveLocalHistoryBatch(List<WeighSession> sessions) async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final List<String> history = prefs.getStringList('mbg_local_history') ?? [];
      for (final s in sessions) {
        final itemMap = {
          'id': s.id,
          'tanggal': s.tanggal,
          'waktu': s.waktu,
          'tim_kerja': s.timKerja,
          'item': s.itemMenu,
          'tahapan': s.tahapan,
          'kategori': s.kategori,
          'total_berat': s.totalNetWeight,
          'wadah_count': s.batchCount,
          'petugas': s.petugas,
        };
        history.insert(0, jsonEncode(itemMap));
      }
      if (history.length > 50) history.removeRange(50, history.length);
      await prefs.setStringList('mbg_local_history', history);
    } catch (_) {}
  }

  static Future<List<Map<String, dynamic>>> getLocalHistory() async {
    final prefs = await SharedPreferences.getInstance();
    final List<String> list = prefs.getStringList('mbg_local_history') ?? [];
    return list.map((item) => jsonDecode(item) as Map<String, dynamic>).toList();
  }
}
