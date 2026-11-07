class WeighBatchItem {
  final String id;
  final double grossWeight;
  final double tareWeight;
  final String? imagePath;
  final DateTime timestamp;
  final bool isManual;
  final double? rawOcrConfidence;

  WeighBatchItem({
    required this.id,
    required this.grossWeight,
    this.tareWeight = 0.0,
    this.imagePath,
    DateTime? timestamp,
    this.isManual = false,
    this.rawOcrConfidence,
  }) : timestamp = timestamp ?? DateTime.now();

  double get netWeight {
    final net = grossWeight - tareWeight;
    return net > 0 ? net : 0.0;
  }

  WeighBatchItem copyWith({
    double? grossWeight,
    double? tareWeight,
    String? imagePath,
    bool? isManual,
  }) {
    return WeighBatchItem(
      id: id,
      grossWeight: grossWeight ?? this.grossWeight,
      tareWeight: tareWeight ?? this.tareWeight,
      imagePath: imagePath ?? this.imagePath,
      timestamp: timestamp,
      isManual: isManual ?? this.isManual,
      rawOcrConfidence: rawOcrConfidence,
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'gross_weight': grossWeight,
    'tare_weight': tareWeight,
    'net_weight': netWeight,
    'image_path': imagePath,
    'timestamp': timestamp.toIso8601String(),
    'is_manual': isManual,
  };

  factory WeighBatchItem.fromJson(Map<String, dynamic> json) => WeighBatchItem(
    id: json['id']?.toString() ?? '',
    grossWeight: (json['gross_weight'] as num?)?.toDouble() ?? 0.0,
    tareWeight: (json['tare_weight'] as num?)?.toDouble() ?? 0.0,
    imagePath: json['image_path']?.toString(),
    timestamp: json['timestamp'] != null
        ? DateTime.tryParse(json['timestamp'].toString()) ?? DateTime.now()
        : DateTime.now(),
    isManual: json['is_manual'] == true,
  );
}

class WeighSession {
  final String id;
  final String tanggal;
  final String waktu;
  final String timKerja;
  final String kategori;
  final String tahapan;
  final String itemMenu;
  final String petugas;
  String? catatan;
  final double defaultTarePerContainer;
  final List<WeighBatchItem> batches;
  List<WeighBatchItem> get batchItems => batches;

  WeighSession({
    required this.id,
    required this.tanggal,
    required this.waktu,
    this.timKerja = 'TIM PERSIAPAN',
    required this.kategori,
    required this.tahapan,
    required this.itemMenu,
    required this.petugas,
    this.catatan,
    this.defaultTarePerContainer = 0.85,
    List<WeighBatchItem>? batches,
    List<WeighBatchItem>? batchItems,
  }) : batches = batches ?? batchItems ?? [];

  double get totalGrossWeight =>
      batches.fold(0.0, (sum, item) => sum + item.grossWeight);

  double get totalTareWeight =>
      batches.fold(0.0, (sum, item) => sum + item.tareWeight);

  double get totalNetWeight =>
      batches.fold(0.0, (sum, item) => sum + item.netWeight);

  int get batchCount => batches.length;

  List<double> get batchWeights =>
      batches.map((b) => double.parse(b.netWeight.toStringAsFixed(2))).toList();

  String get indonesianDayName {
    try {
      final dt = DateTime.parse(tanggal);
      const days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"];
      final day = days[dt.weekday - 1];
      if (day == "Sabtu" || day == "Minggu") return "Senin";
      return day;
    } catch (_) {
      return "Senin";
    }
  }

  Map<String, dynamic> toWebhookPayload() => {
    'hari': indonesianDayName,
    'tanggal': tanggal,
    'waktu': waktu,
    'tim_kerja': timKerja,
    'kategori': kategori,
    'item': itemMenu,
    'tahapan': tahapan,
    'total_berat': double.parse(totalNetWeight.toStringAsFixed(2)),
    'total_bruto': double.parse(totalGrossWeight.toStringAsFixed(2)),
    'total_tara': double.parse(totalTareWeight.toStringAsFixed(2)),
    'jumlah_wadah': batchCount,
    'batch_detail': batchWeights,
    'catatan': catatan ?? '',
    'petugas': petugas,
  };
}

class TeamBatchStaging {
  final String teamName;
  final List<WeighSession> sessions;

  TeamBatchStaging({
    required this.teamName,
    required this.sessions,
  });

  double get grandTotalNet =>
      sessions.fold(0.0, (sum, s) => sum + s.totalNetWeight);

  int get totalContainers =>
      sessions.fold(0, (sum, s) => sum + s.batchCount);

  Map<String, dynamic> toBatchWebhookPayload() => {
    'hari': sessions.isNotEmpty ? sessions.first.indonesianDayName : 'Senin',
    'tim_kerja': teamName,
    'total_item': sessions.length,
    'grand_total_netto': double.parse(grandTotalNet.toStringAsFixed(2)),
    'batch_sessions': sessions.map((s) => s.toWebhookPayload()).toList(),
  };
}

class WarehouseStockItem {
  final String item;
  final String kategori;
  final double totalMasuk;
  final double totalKeluar;
  final double sisaBalik;
  final double limbah;
  final double stokTersedia;
  final String status;
  final String lastUpdated;

  String get namaBahan => item;

  WarehouseStockItem({
    required this.item,
    required this.kategori,
    required this.totalMasuk,
    required this.totalKeluar,
    required this.sisaBalik,
    required this.limbah,
    required this.stokTersedia,
    required this.status,
    required this.lastUpdated,
  });

  factory WarehouseStockItem.fromJson(Map<String, dynamic> json) => WarehouseStockItem(
    item: json['item']?.toString() ?? '',
    kategori: json['kategori']?.toString() ?? '',
    totalMasuk: (json['total_masuk'] as num?)?.toDouble() ?? 0.0,
    totalKeluar: (json['total_keluar'] as num?)?.toDouble() ?? 0.0,
    sisaBalik: (json['sisa_balik'] as num?)?.toDouble() ?? 0.0,
    limbah: (json['limbah'] as num?)?.toDouble() ?? 0.0,
    stokTersedia: (json['stok_tersedia'] as num?)?.toDouble() ?? 0.0,
    status: json['status']?.toString() ?? 'Tersedia',
    lastUpdated: json['last_updated']?.toString() ?? '',
  );
}
