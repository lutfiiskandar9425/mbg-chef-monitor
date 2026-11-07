import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'package:image_picker/image_picker.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/weigh_batch.dart';
import '../services/sheets_service.dart';
import 'camera_batch_screen.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> with SingleTickerProviderStateMixin {
  late TabController _tabController;
  final ImagePicker _picker = ImagePicker();

  final TextEditingController _itemController = TextEditingController();
  final TextEditingController _petugasController = TextEditingController();
  final TextEditingController _tareController = TextEditingController(text: "0.85");

  String _selectedTim = 'TIM PERSIAPAN';
  String _selectedTahapan = 'Penerimaan (Datang ke Gudang)';
  String _selectedKategori = 'Sayuran Segar';
  DateTime _selectedDate = DateTime.now();

  final List<String> _timList = [
    'TIM PERSIAPAN',
    'TIM PENGOLAHAN',
    'TIM PEMORSIAN',
  ];

  final List<String> _tahapanList = [
    'Penerimaan (Datang ke Gudang)',
    'Pengeluaran (Gudang ke Dapur Masak)',
    'Sisa Olahan (Kembali ke Gudang / Next Menu)',
    'Limbah & Susut (Waste Non-Reusable)',
  ];

  final List<String> _kategoriList = [
    'Sayuran Segar',
    'Protein Hewani',
    'Protein Nabati',
    'Beras & Karbohidrat',
    'Buah Segar',
    'Saos & Sambal (Pelengkap)',
    'Bumbu & Bahan Kering',
    'Buah & Pelengkap',
  ];

  final Map<String, List<String>> _quickItems = {
    'Protein Hewani': [
      'Telur Ayam Rollade Bulat',
      'Chicken Drum Stick',
      'Bola Bakso Daging Sapi (Isi 3)',
      'Telor Ceplok (Mata Sapi)',
      'Telur Katsu Krispi',
      'Ikan Lele Crispy (Fillet)',
      'Ayam Ungkep Bumbu Hitam',
      'Telur Dadar Fuyunghai',
      'Semur Telur Dadar Gulung',
      'Daging Ayam Fillet',
      'Daging Sapi Segar',
    ],
    'Beras & Karbohidrat': [
      'Beras Putih (Nasi Gurih)',
      'Beras Putih Premium',
      'Roti Tawar Lembaran (2 Tangkup)',
      'Beras Medium SPPG',
    ],
    'Protein Nabati': [
      'Edamame Segar Rebus',
      'Stik Tempe Tepung',
      'Tahu Putih Goreng Gurih',
      'Tempe Orek Kacang Panjang',
      'Tempe Goreng Ketumbar',
      'Tempe Kedelai Segar',
      'Tahu Putih Sutra',
    ],
    'Sayuran Segar': [
      'Kakiage (Bakwan Jepang)',
      'Mix Vigie (Jagung Polong Wortel)',
      'Tumis Kol & Wortel',
      'Timun & Selada Segar Higienis',
      'Tumis Labu Siam Jagung Pipil',
      'Lalap Timun + Labu Siam Kukus',
      'Kacang Polong & Wortel Rebus',
      'Gyoza Sayur (Wortel & Kol)',
      'Wortel Brastagi',
      'Buncis Baby',
    ],
    'Saos & Sambal (Pelengkap)': [
      'Sambal Bawang Tanak',
      'Saus BBQ Racikan Dapur',
      'Saus Bangkok Asam Manis',
      'Saus Mayo Pedas Gurih',
      'Sambal Bajak Matang',
      'Sambal Kecap Rawit Bawang',
      'Saus Asam Manis Fuyunghai',
      'Sambal Terasi',
    ],
    'Buah Segar': [
      'Jeruk Manis Segar',
      'Semangka Merah Potong',
      'Pisang Cavendish Standar BGN',
      'Melon Cantaloupe Segar',
      'Kelengkeng Manis Segar',
      'Buah Naga Merah Dadu',
    ],
    'Bumbu & Bahan Kering': [
      'Bawang Merah Kupas',
      'Bawang Putih Kating',
      'Cabai Merah Keriting',
      'Minyak Goreng Sawit',
      'Garam Dapur Halus',
      'Gula Pasir',
    ],
    'Buah & Pelengkap': [
      'Jeruk Manis Segar',
      'Semangka Merah Potong',
      'Pisang Cavendish Standar BGN',
      'Melon Cantaloupe Segar',
      'Kelengkeng Manis Segar',
      'Buah Naga Merah Dadu',
    ],
  };

  final Map<String, List<WeighSession>> _teamStagingMap = {
    'TIM PERSIAPAN': [],
    'TIM PENGOLAHAN': [],
    'TIM PEMORSIAN': [],
  };

  bool _isSyncingTeamBatch = false;
  List<WarehouseStockItem> _warehouseStock = [];
  bool _isLoadingStock = false;
  List<Map<String, dynamic>> _historyLogs = [];
  bool _isLoadingHistory = false;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 4, vsync: this);
    WidgetsBinding.instance.addPostFrameCallback((_) {
      _loadSavedPreferences();
      _loadWarehouseStock();
      _loadHistory();
    });
  }

  void _onTimSelected(String tim) {
    setState(() {
      _selectedTim = tim;
      if (tim == 'TIM PERSIAPAN') {
        _selectedTahapan = 'Penerimaan (Datang ke Gudang)';
        _selectedKategori = 'Sayuran Segar';
      } else if (tim == 'TIM PENGOLAHAN (PROHE)') {
        _selectedTahapan = 'Pengeluaran (Gudang ke Dapur Masak)';
        _selectedKategori = 'Protein Hewani';
      } else if (tim == 'TIM PENGOLAHAN (PRONA)') {
        _selectedTahapan = 'Pengeluaran (Gudang ke Dapur Masak)';
        _selectedKategori = 'Protein Nabati';
      } else if (tim == 'TIM PENGOLAHAN (SAYUR)') {
        _selectedTahapan = 'Pengeluaran (Gudang ke Dapur Masak)';
        _selectedKategori = 'Sayuran Segar';
      } else if (tim == 'TIM PENGOLAHAN (SAOS / SAMBAL)') {
        _selectedTahapan = 'Pengeluaran (Gudang ke Dapur Masak)';
        _selectedKategori = 'Saos & Sambal (Pelengkap)';
      } else if (tim == 'TIM BUAH & POTONG') {
        _selectedTahapan = 'Penerimaan (Datang ke Gudang)';
        _selectedKategori = 'Buah Segar';
      } else if (tim == 'TIM PEMORSIAN') {
        _selectedTahapan = 'Pengeluaran (Gudang ke Dapur Masak)';
        _selectedKategori = 'Beras & Karbohidrat';
      }

      if (_quickItems[_selectedKategori]?.isNotEmpty ?? false) {
        _itemController.text = _quickItems[_selectedKategori]!.first;
      }
    });
  }

  Future<void> _loadSavedPreferences() async {
    final prefs = await SharedPreferences.getInstance();
    final savedPetugas = prefs.getString('mbg_petugas_name') ?? 'Head Chef Lutfi';
    final savedTare = prefs.getDouble('mbg_default_tare') ?? 0.85;
    setState(() {
      _petugasController.text = savedPetugas;
      _tareController.text = savedTare.toStringAsFixed(2);
      if (_quickItems[_selectedKategori]?.isNotEmpty ?? false) {
        _itemController.text = _quickItems[_selectedKategori]!.first;
      }
    });
  }

  Future<void> _loadWarehouseStock() async {
    setState(() => _isLoadingStock = true);
    final stock = await SheetsService.fetchWarehouseStock();
    setState(() {
      _warehouseStock = stock;
      _isLoadingStock = false;
    });
  }

  Future<void> _loadHistory() async {
    setState(() => _isLoadingHistory = true);
    final logs = await SheetsService.getLocalHistory();
    setState(() {
      _historyLogs = logs;
      _isLoadingHistory = false;
    });
  }

  Future<void> _savePreferences() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString('mbg_petugas_name', _petugasController.text.trim());
    final tare = double.tryParse(_tareController.text.replaceAll(',', '.')) ?? 0.0;
    await prefs.setDouble('mbg_default_tare', tare);
  }

  void _openSettingsDialog() async {
    final currentUrl = await SheetsService.getWebhookUrl();
    final urlController = TextEditingController(text: currentUrl);

    if (!mounted) return;
    showDialog(
      context: context,
      builder: (ctx) => AlertDialog(
        backgroundColor: Colors.white,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
        title: const Text(
          "Pengaturan Webhook SPPG",
          style: TextStyle(fontWeight: FontWeight.w700, fontSize: 18),
        ),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              "URL Webhook Google Apps Script:",
              style: TextStyle(fontSize: 13, color: Color(0xFF64748B)),
            ),
            const SizedBox(height: 8),
            TextField(
              controller: urlController,
              decoration: const InputDecoration(
                hintText: "https://script.google.com/macros/s/.../exec",
              ),
              maxLines: 3,
            ),
          ],
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(ctx),
            child: const Text("Batal", style: TextStyle(color: Color(0xFF64748B))),
          ),
          ElevatedButton(
            onPressed: () async {
              await SheetsService.saveWebhookUrl(urlController.text);
              if (ctx.mounted) Navigator.pop(ctx);
              if (mounted) {
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(
                    content: Text("URL Webhook berhasil diperbarui."),
                    behavior: SnackBarBehavior.floating,
                  ),
                );
                _loadWarehouseStock();
              }
            },
            child: const Text("Simpan"),
          ),
        ],
      ),
    );
  }

  /// Memulai sesi timbang: bisa dari KAMERA langsung atau dari GALERI foto
  void _startWeighingSession({bool fromGallery = false}) async {
    if (_itemController.text.trim().isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text("Harap isi nama bahan terlebih dahulu."),
          behavior: SnackBarBehavior.floating,
        ),
      );
      return;
    }

    await _savePreferences();
    final double defaultTare =
        double.tryParse(_tareController.text.replaceAll(',', '.')) ?? 0.0;

    String? pickedImagePath;
    if (fromGallery) {
      final XFile? photo = await _picker.pickImage(
        source: ImageSource.gallery,
        imageQuality: 92,
      );
      if (photo == null) return;
      pickedImagePath = photo.path;
    }

    if (!mounted) return;
    final WeighSession? completedSession = await Navigator.push<WeighSession>(
      context,
      MaterialPageRoute(
        builder: (_) => CameraBatchScreen(
          tanggal: DateFormat('yyyy-MM-dd').format(_selectedDate),
          kategori: _selectedKategori,
          tahapan: _selectedTahapan,
          itemMenu: _itemController.text.trim(),
          petugas: _petugasController.text.trim().isEmpty ? 'Petugas' : _petugasController.text.trim(),
          defaultTarePerBatch: defaultTare,
          initialImagePath: pickedImagePath,
        ),
      ),
    );

    if (completedSession != null) {
      final sessionWithTeam = WeighSession(
        id: completedSession.id,
        tanggal: completedSession.tanggal,
        waktu: completedSession.waktu,
        timKerja: _selectedTim,
        kategori: completedSession.kategori,
        tahapan: completedSession.tahapan,
        itemMenu: completedSession.itemMenu,
        petugas: completedSession.petugas,
        catatan: completedSession.catatan,
        defaultTarePerContainer: completedSession.defaultTarePerContainer,
        batches: completedSession.batches,
      );

      setState(() {
        _teamStagingMap[_selectedTim]?.add(sessionWithTeam);
      });

      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text("${sessionWithTeam.itemMenu} (${sessionWithTeam.totalNetWeight.toStringAsFixed(2)} kg) masuk keranjang $_selectedTim."),
          behavior: SnackBarBehavior.floating,
          action: SnackBarAction(
            label: "Keranjang",
            onPressed: () => _tabController.animateTo(1),
          ),
        ),
      );
    }
  }

  Future<void> _submitActiveTeamBatch() async {
    final List<WeighSession> sessions = _teamStagingMap[_selectedTim] ?? [];
    if (sessions.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text("Keranjang $_selectedTim masih kosong."),
          behavior: SnackBarBehavior.floating,
        ),
      );
      return;
    }

    setState(() => _isSyncingTeamBatch = true);

    final teamBatch = TeamBatchStaging(
      teamName: _selectedTim,
      sessions: List.from(sessions),
    );

    final result = await SheetsService.syncTeamBatch(teamBatch);

    if (!mounted) return;
    setState(() => _isSyncingTeamBatch = false);

    if (result.isSuccess) {
      await SheetsService.saveLocalHistoryBatch(sessions);
      setState(() {
        _teamStagingMap[_selectedTim]?.clear();
      });

      showDialog(
        context: context,
        builder: (ctx) => AlertDialog(
          backgroundColor: Colors.white,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
          title: Row(
            children: [
              const Icon(Icons.check_circle, color: Color(0xFF059669), size: 28),
              const SizedBox(width: 10),
              const Text("Terkirim ke Sheet", style: TextStyle(fontWeight: FontWeight.w700)),
            ],
          ),
          content: Text("Data dari $_selectedTim (${sessions.length} bahan, total ${teamBatch.grandTotalNet.toStringAsFixed(2)} kg) telah resmi masuk ke Formulir Alur Bahan Baku Google Sheets SPPG."),
          actions: [
            ElevatedButton(
              style: ElevatedButton.styleFrom(
                backgroundColor: const Color(0xFF0F172A),
                foregroundColor: Colors.white,
              ),
              onPressed: () {
                Navigator.pop(ctx);
                _loadHistory();
                _loadWarehouseStock();
              },
              child: const Text("Selesai"),
            ),
          ],
        ),
      );
    } else {
      showDialog(
        context: context,
        builder: (ctx) => AlertDialog(
          backgroundColor: Colors.white,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
          title: const Text("Pengiriman Gagal"),
          content: Text(result.message),
          actions: [
            TextButton(
              onPressed: () => Navigator.pop(ctx),
              child: const Text("Tutup", style: TextStyle(color: Color(0xFF64748B))),
            ),
          ],
        ),
      );
    }
  }

  @override
  void dispose() {
    _tabController.dispose();
    _itemController.dispose();
    _petugasController.dispose();
    _tareController.dispose();
    super.dispose();
  }

  String _formatIndonesianDate(DateTime date) {
    const days = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'];
    const months = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'];
    final dayName = days[(date.weekday - 1).clamp(0, 6)];
    final monthName = months[date.month.clamp(1, 12)];
    return '$dayName, ${date.day} $monthName ${date.year}';
  }

  @override
  Widget build(BuildContext context) {
    final currentStagingCount = (_teamStagingMap[_selectedTim] ?? []).length;

    return Scaffold(
      backgroundColor: const Color(0xFFF8FAFC),
      appBar: AppBar(
        leadingWidth: 54,
        leading: Padding(
          padding: const EdgeInsets.only(left: 16, top: 8, bottom: 8),
          child: Image.asset(
            'assets/images/bgn_logo.png',
            fit: BoxFit.contain,
            errorBuilder: (_, __, ___) => Container(
              decoration: const BoxDecoration(
                color: Color(0xFF0F172A),
                shape: BoxShape.circle,
              ),
              alignment: Alignment.center,
              child: const Text('BGN', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 10)),
            ),
          ),
        ),
        title: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              "MBG Chef Monitor",
              style: TextStyle(
                fontWeight: FontWeight.w800,
                fontSize: 19,
                color: Color(0xFF0F172A),
                letterSpacing: -0.5,
              ),
            ),
            Row(
              children: [
                Container(
                  width: 7,
                  height: 7,
                  decoration: const BoxDecoration(
                    color: Color(0xFF10B981),
                    shape: BoxShape.circle,
                  ),
                ),
                const SizedBox(width: 6),
                const Text(
                  "SPPG Pekajangan 4 • Sheet Live",
                  style: TextStyle(fontSize: 11, color: Color(0xFF64748B), fontWeight: FontWeight.w500),
                ),
              ],
            ),
          ],
        ),
        actions: [
          IconButton(
            icon: const Icon(Icons.tune_outlined, color: Color(0xFF334155)),
            tooltip: "Pengaturan Webhook",
            onPressed: _openSettingsDialog,
          ),
        ],
        bottom: PreferredSize(
          preferredSize: const Size.fromHeight(48),
          child: Container(
            margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 4),
            decoration: BoxDecoration(
              color: const Color(0xFFF1F5F9),
              borderRadius: BorderRadius.circular(12),
            ),
            child: TabBar(
              controller: _tabController,
              indicatorSize: TabBarIndicatorSize.tab,
              dividerColor: Colors.transparent,
              indicator: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(10),
                boxShadow: [
                  BoxShadow(
                    color: Colors.black.withOpacity(0.04),
                    blurRadius: 4,
                    offset: const Offset(0, 2),
                  ),
                ],
              ),
              labelColor: const Color(0xFF0F172A),
              unselectedLabelColor: const Color(0xFF64748B),
              labelStyle: const TextStyle(fontSize: 12, fontWeight: FontWeight.w700),
              unselectedLabelStyle: const TextStyle(fontSize: 12, fontWeight: FontWeight.w500),
              tabs: [
                const Tab(text: "Timbang"),
                Tab(
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      const Text("Keranjang"),
                      if (currentStagingCount > 0) ...[
                        const SizedBox(width: 4),
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                          decoration: const BoxDecoration(
                            color: Color(0xFF059669),
                            shape: BoxShape.circle,
                          ),
                          child: Text(
                            "$currentStagingCount",
                            style: const TextStyle(color: Colors.white, fontSize: 10, fontWeight: FontWeight.bold),
                          ),
                        ),
                      ],
                    ],
                  ),
                ),
                const Tab(text: "Gudang"),
                const Tab(text: "Riwayat"),
              ],
            ),
          ),
        ),
      ),
      body: TabBarView(
        controller: _tabController,
        children: [
          _buildWeighFormTab(),
          _buildTeamCartTab(),
          _buildWarehouseStockTab(),
          _buildHistoryTab(),
        ],
      ),
    );
  }

  Widget _buildWeighFormTab() {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // STASIUN TIM SELECTOR (MODERN HORIZONTAL PILLS)
          const Text(
            "STASIUN / TIM KERJA",
            style: TextStyle(fontSize: 11, fontWeight: FontWeight.w700, letterSpacing: 1.1, color: Color(0xFF64748B)),
          ),
          const SizedBox(height: 8),
          SingleChildScrollView(
            scrollDirection: Axis.horizontal,
            child: Row(
              children: _timList.map((tim) {
                final isSelected = _selectedTim == tim;
                final itemCount = _teamStagingMap[tim]?.length ?? 0;
                return Padding(
                  padding: const EdgeInsets.only(right: 8),
                  child: FilterChip(
                    showCheckmark: false,
                    selected: isSelected,
                    selectedColor: const Color(0xFF0F172A),
                    backgroundColor: Colors.white,
                    side: BorderSide(
                      color: isSelected ? const Color(0xFF0F172A) : const Color(0xFFE2E8F0),
                    ),
                    label: Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Text(
                          tim,
                          style: TextStyle(
                            fontSize: 12,
                            fontWeight: isSelected ? FontWeight.w700 : FontWeight.w600,
                            color: isSelected ? Colors.white : const Color(0xFF334155),
                          ),
                        ),
                        if (itemCount > 0) ...[
                          const SizedBox(width: 6),
                          Container(
                            padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                            decoration: BoxDecoration(
                              color: isSelected ? const Color(0xFF059669) : const Color(0xFFE2E8F0),
                              borderRadius: BorderRadius.circular(10),
                            ),
                            child: Text(
                              "$itemCount",
                              style: TextStyle(
                                fontSize: 10,
                                fontWeight: FontWeight.bold,
                                color: isSelected ? Colors.white : const Color(0xFF0F172A),
                              ),
                            ),
                          ),
                        ],
                      ],
                    ),
                    onSelected: (_) => _onTimSelected(tim),
                  ),
                );
              }).toList(),
            ),
          ),
          const SizedBox(height: 16),

          // CARD UTAMA INPUT TIMBANG (MODERN MINIMALIST)
          Container(
            padding: const EdgeInsets.all(20),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(20),
              border: Border.all(color: const Color(0xFFE2E8F0)),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // TANGGAL & TAHAPAN
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(
                      _formatIndonesianDate(_selectedDate),
                      style: const TextStyle(fontWeight: FontWeight.w700, fontSize: 14, color: Color(0xFF0F172A)),
                    ),
                    InkWell(
                      onTap: () async {
                        final picked = await showDatePicker(
                          context: context,
                          initialDate: _selectedDate,
                          firstDate: DateTime(2024),
                          lastDate: DateTime(2030),
                        );
                        if (picked != null) setState(() => _selectedDate = picked);
                      },
                      child: const Text("Ubah", style: TextStyle(color: Color(0xFF059669), fontWeight: FontWeight.w600, fontSize: 13)),
                    ),
                  ],
                ),
                const SizedBox(height: 14),

                // KATEGORI KOMODITAS
                const Text("Kategori Bahan:", style: TextStyle(fontSize: 12, fontWeight: FontWeight.w600, color: Color(0xFF64748B))),
                const SizedBox(height: 6),
                DropdownButtonFormField<String>(
                  value: _selectedKategori,
                  decoration: const InputDecoration(contentPadding: EdgeInsets.symmetric(horizontal: 14, vertical: 12)),
                  items: _kategoriList.map((k) => DropdownMenuItem(value: k, child: Text(k, style: const TextStyle(fontSize: 14)))).toList(),
                  onChanged: (val) {
                    if (val != null) {
                      setState(() {
                        _selectedKategori = val;
                        if (_quickItems[val]?.isNotEmpty ?? false) {
                          _itemController.text = _quickItems[val]!.first;
                        }
                      });
                    }
                  },
                ),
                const SizedBox(height: 14),

                // NAMA BAHAN BAKU
                const Text("Nama Bahan Baku:", style: TextStyle(fontSize: 12, fontWeight: FontWeight.w600, color: Color(0xFF64748B))),
                const SizedBox(height: 6),
                TextField(
                  controller: _itemController,
                  style: const TextStyle(fontSize: 15, fontWeight: FontWeight.w600),
                  decoration: const InputDecoration(
                    hintText: "Ketik nama bahan (contoh: Wortel, Daging Ayam...)",
                  ),
                ),
                const SizedBox(height: 10),

                // QUICK CHIPS BAHAN
                if (_quickItems[_selectedKategori]?.isNotEmpty ?? false)
                  Wrap(
                    spacing: 6,
                    runSpacing: 6,
                    children: _quickItems[_selectedKategori]!.map((item) {
                      final isCurrent = _itemController.text == item;
                      return ActionChip(
                        label: Text(item, style: TextStyle(fontSize: 11, fontWeight: isCurrent ? FontWeight.bold : FontWeight.normal)),
                        backgroundColor: isCurrent ? const Color(0xFFE2E8F0) : const Color(0xFFF8FAFC),
                        side: BorderSide(color: isCurrent ? const Color(0xFF0F172A) : const Color(0xFFE2E8F0)),
                        onPressed: () => setState(() => _itemController.text = item),
                      );
                    }).toList(),
                  ),
                const SizedBox(height: 16),

                // TARA WADAH (KG)
                Row(
                  crossAxisAlignment: CrossAxisAlignment.end,
                  children: [
                    Expanded(
                      flex: 3,
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          const Text("Tara Wadah (kg):", style: TextStyle(fontSize: 12, fontWeight: FontWeight.w600, color: Color(0xFF64748B))),
                          const SizedBox(height: 6),
                          TextField(
                            controller: _tareController,
                            keyboardType: const TextInputType.numberWithOptions(decimal: true),
                            decoration: const InputDecoration(suffixText: "kg"),
                          ),
                        ],
                      ),
                    ),
                    const SizedBox(width: 10),
                    Expanded(
                      flex: 4,
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          const Text("Preset Tara:", style: TextStyle(fontSize: 12, fontWeight: FontWeight.w600, color: Color(0xFF64748B))),
                          const SizedBox(height: 6),
                          Row(
                            children: [
                              _buildPresetTareChip("0.85"),
                              const SizedBox(width: 6),
                              _buildPresetTareChip("0.50"),
                              const SizedBox(width: 6),
                              _buildPresetTareChip("0.00"),
                            ],
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 16),

                // PETUGAS / CHEF
                const Text("Petugas / Chef QC:", style: TextStyle(fontSize: 12, fontWeight: FontWeight.w600, color: Color(0xFF64748B))),
                const SizedBox(height: 6),
                TextField(
                  controller: _petugasController,
                  decoration: const InputDecoration(hintText: "Nama chef yang bertugas"),
                ),
              ],
            ),
          ),
          const SizedBox(height: 20),

          // DUA ACTION BUTTON: KAMERA & GALERI (MODERN & ERGONOMIC)
          Row(
            children: [
              // TOMBOL FOTO KAMERA LANGSUNG
              Expanded(
                child: SizedBox(
                  height: 52,
                  child: ElevatedButton.icon(
                    style: ElevatedButton.styleFrom(
                      backgroundColor: const Color(0xFF0F172A),
                      foregroundColor: Colors.white,
                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
                    ),
                    onPressed: () => _startWeighingSession(fromGallery: false),
                    icon: const Icon(Icons.camera_alt_outlined, size: 20),
                    label: const Text(
                      "Foto Kamera",
                      style: TextStyle(fontSize: 15, fontWeight: FontWeight.w700),
                    ),
                  ),
                ),
              ),
              const SizedBox(width: 12),

              // TOMBOL AMBIL DARI GALERI HP
              Expanded(
                child: SizedBox(
                  height: 52,
                  child: OutlinedButton.icon(
                    style: OutlinedButton.styleFrom(
                      backgroundColor: Colors.white,
                      foregroundColor: const Color(0xFF0F172A),
                      side: const BorderSide(color: Color(0xFF0F172A), width: 1.5),
                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
                    ),
                    onPressed: () => _startWeighingSession(fromGallery: true),
                    icon: const Icon(Icons.photo_library_outlined, size: 20),
                    label: const Text(
                      "Ambil di Galeri",
                      style: TextStyle(fontSize: 15, fontWeight: FontWeight.w700),
                    ),
                  ),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }

  Widget _buildPresetTareChip(String val) {
    final isSelected = _tareController.text == val;
    return Expanded(
      child: InkWell(
        onTap: () => setState(() => _tareController.text = val),
        borderRadius: BorderRadius.circular(8),
        child: Container(
          padding: const EdgeInsets.symmetric(vertical: 13),
          alignment: Alignment.center,
          decoration: BoxDecoration(
            color: isSelected ? const Color(0xFF0F172A) : const Color(0xFFF1F5F9),
            borderRadius: BorderRadius.circular(10),
            border: Border.all(color: isSelected ? const Color(0xFF0F172A) : const Color(0xFFE2E8F0)),
          ),
          child: Text(
            val == "0.00" ? "Nol" : val,
            style: TextStyle(
              fontSize: 12,
              fontWeight: FontWeight.w700,
              color: isSelected ? Colors.white : const Color(0xFF334155),
            ),
          ),
        ),
      ),
    );
  }

  void _showEditCartDialog(List<WeighSession> sessions, int idx) {
    final s = sessions[idx];
    final itemController = TextEditingController(text: s.itemMenu);
    final noteController = TextEditingController(text: s.catatan ?? '');

    showDialog(
      context: context,
      builder: (ctx) => AlertDialog(
        backgroundColor: Colors.white,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
        title: const Text("Edit Bahan Keranjang", style: TextStyle(fontWeight: FontWeight.bold, fontSize: 17)),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text("Nama Bahan Baku:", style: TextStyle(fontSize: 12, color: Color(0xFF64748B))),
            const SizedBox(height: 4),
            TextField(
              controller: itemController,
              decoration: InputDecoration(
                filled: true,
                fillColor: const Color(0xFFF8FAFC),
                border: OutlineInputBorder(borderRadius: BorderRadius.circular(12), borderSide: BorderSide.none),
              ),
            ),
            const SizedBox(height: 12),
            const Text("Catatan / Keterangan QC:", style: TextStyle(fontSize: 12, color: Color(0xFF64748B))),
            const SizedBox(height: 4),
            TextField(
              controller: noteController,
              decoration: InputDecoration(
                filled: true,
                fillColor: const Color(0xFFF8FAFC),
                border: OutlineInputBorder(borderRadius: BorderRadius.circular(12), borderSide: BorderSide.none),
              ),
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
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
            ),
            onPressed: () {
              setState(() {
                sessions[idx] = WeighSession(
                  id: s.id,
                  tanggal: s.tanggal,
                  waktu: s.waktu,
                  timKerja: s.timKerja,
                  kategori: s.kategori,
                  tahapan: s.tahapan,
                  itemMenu: itemController.text.trim().isEmpty ? s.itemMenu : itemController.text.trim(),
                  petugas: s.petugas,
                  catatan: noteController.text.trim(),
                  defaultTarePerContainer: s.defaultTarePerContainer,
                  batches: s.batches,
                );
              });
              Navigator.pop(ctx);
            },
            child: const Text("Simpan"),
          ),
        ],
      ),
    );
  }

  void _confirmDeleteCartItem(List<WeighSession> sessions, int idx) {
    final item = sessions[idx];
    showDialog(
      context: context,
      builder: (ctx) => AlertDialog(
        backgroundColor: Colors.white,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
        title: const Text("Hapus dari Keranjang?", style: TextStyle(fontWeight: FontWeight.bold, fontSize: 17)),
        content: Text("Yakin ingin menghapus ${item.itemMenu} (${item.totalNetWeight.toStringAsFixed(2)} kg)?"),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(ctx),
            child: const Text("Batal", style: TextStyle(color: Color(0xFF64748B))),
          ),
          ElevatedButton(
            style: ElevatedButton.styleFrom(
              backgroundColor: const Color(0xFFEF4444),
              foregroundColor: Colors.white,
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
            ),
            onPressed: () {
              setState(() => sessions.removeAt(idx));
              Navigator.pop(ctx);
            },
            child: const Text("Hapus"),
          ),
        ],
      ),
    );
  }

  // TAB 2: KERANJANG STAGING BATCH TIM
  Widget _buildTeamCartTab() {
    final sessions = _teamStagingMap[_selectedTim] ?? [];
    final totalTeamNet = sessions.fold(0.0, (sum, s) => sum + s.totalNetWeight);
    final totalWadah = sessions.fold(0, (sum, s) => sum + s.batchCount);

    return Column(
      children: [
        // RINGKASAN KERANJANG HERO CARD
        Container(
          margin: const EdgeInsets.all(16),
          padding: const EdgeInsets.all(20),
          decoration: BoxDecoration(
            color: const Color(0xFF0F172A),
            borderRadius: BorderRadius.circular(20),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Text(
                    _selectedTim,
                    style: const TextStyle(fontSize: 12, fontWeight: FontWeight.w700, color: Color(0xFF94A3B8), letterSpacing: 1.1),
                  ),
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                    decoration: BoxDecoration(
                      color: const Color(0xFF1E293B),
                      borderRadius: BorderRadius.circular(20),
                    ),
                    child: Text(
                      "${sessions.length} Bahan",
                      style: const TextStyle(color: Colors.white, fontSize: 11, fontWeight: FontWeight.w600),
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
                    totalTeamNet.toStringAsFixed(2),
                    style: const TextStyle(fontSize: 38, fontWeight: FontWeight.w800, color: Colors.white, letterSpacing: -1),
                  ),
                  const SizedBox(width: 6),
                  const Text("kg (Netto)", style: TextStyle(fontSize: 16, color: Color(0xFF10B981), fontWeight: FontWeight.w700)),
                  const Spacer(),
                  Text("$totalWadah Total Wadah", style: const TextStyle(color: Color(0xFF94A3B8), fontSize: 13)),
                ],
              ),
            ],
          ),
        ),

        // DAFTAR ITEM DI KERANJANG
        Expanded(
          child: sessions.isEmpty
              ? Center(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Icon(Icons.shopping_basket_outlined, size: 52, color: Colors.grey.shade400),
                      const SizedBox(height: 12),
                      Text("Keranjang $_selectedTim Kosong", style: const TextStyle(fontSize: 15, fontWeight: FontWeight.w700, color: Color(0xFF64748B))),
                      const SizedBox(height: 4),
                      const Text("Lakukan timbang bahan di tab 'Timbang' terlebih dahulu", style: TextStyle(fontSize: 12, color: Color(0xFF94A3B8))),
                    ],
                  ),
                )
              : ListView.builder(
                  padding: const EdgeInsets.symmetric(horizontal: 16),
                  itemCount: sessions.length,
                  itemBuilder: (ctx, idx) {
                    final s = sessions[idx];
                    return Container(
                      margin: const EdgeInsets.only(bottom: 10),
                      padding: const EdgeInsets.all(16),
                      decoration: BoxDecoration(
                        color: Colors.white,
                        borderRadius: BorderRadius.circular(16),
                        border: Border.all(color: const Color(0xFFE2E8F0)),
                      ),
                      child: Row(
                        children: [
                          Expanded(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Row(
                                  children: [
                                    Text(s.itemMenu, style: const TextStyle(fontSize: 15, fontWeight: FontWeight.w700, color: Color(0xFF0F172A))),
                                    const SizedBox(width: 8),
                                    Container(
                                      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                                      decoration: BoxDecoration(color: const Color(0xFFF1F5F9), borderRadius: BorderRadius.circular(10)),
                                      child: Text(s.kategori, style: const TextStyle(fontSize: 10, fontWeight: FontWeight.w600)),
                                    ),
                                  ],
                                ),
                                const SizedBox(height: 4),
                                Text(
                                  "Netto: ${s.totalNetWeight.toStringAsFixed(2)} kg  •  ${s.batchCount} wadah",
                                  style: const TextStyle(fontSize: 13, fontWeight: FontWeight.w600, color: Color(0xFF059669)),
                                ),
                                if (s.catatan != null && s.catatan!.isNotEmpty)
                                  Text("Ket: ${s.catatan!}", style: const TextStyle(fontSize: 11, color: Color(0xFF64748B))),
                              ],
                            ),
                          ),
                          IconButton(
                            icon: const Icon(Icons.edit_outlined, color: Color(0xFF64748B)),
                            tooltip: "Edit Bahan",
                            onPressed: () => _showEditCartDialog(sessions, idx),
                          ),
                          IconButton(
                            icon: const Icon(Icons.delete_outline, color: Color(0xFFEF4444)),
                            tooltip: "Hapus Bahan",
                            onPressed: () => _confirmDeleteCartItem(sessions, idx),
                          ),
                        ],
                      ),
                    );
                  },
                ),
        ),

        // TOMBOL KIRIM KE GOOGLE SHEET
        Container(
          padding: const EdgeInsets.all(16),
          decoration: const BoxDecoration(
            color: Colors.white,
            border: Border(top: BorderSide(color: Color(0xFFE2E8F0))),
          ),
          child: SafeArea(
            child: SizedBox(
              width: double.infinity,
              height: 52,
              child: ElevatedButton.icon(
                style: ElevatedButton.styleFrom(
                  backgroundColor: const Color(0xFF059669),
                  foregroundColor: Colors.white,
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
                ),
                onPressed: sessions.isEmpty || _isSyncingTeamBatch ? null : _submitActiveTeamBatch,
                icon: _isSyncingTeamBatch
                    ? const SizedBox(width: 20, height: 20, child: CircularProgressIndicator(strokeWidth: 2, color: Colors.white))
                    : const Icon(Icons.cloud_upload_outlined),
                label: Text(
                  _isSyncingTeamBatch
                      ? "Menyinkronkan ke Google Sheet..."
                      : "Kirim ${sessions.length} Bahan ke Google Sheet",
                  style: const TextStyle(fontSize: 15, fontWeight: FontWeight.w700),
                ),
              ),
            ),
          ),
        ),
      ],
    );
  }

  // TAB 3: STOK GUDANG
  Widget _buildWarehouseStockTab() {
    return Column(
      children: [
        Padding(
          padding: const EdgeInsets.all(16.0),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              const Text("Kartu Stok Gudang", style: TextStyle(fontSize: 16, fontWeight: FontWeight.w700)),
              IconButton(
                icon: const Icon(Icons.refresh, color: Color(0xFF0F172A)),
                onPressed: _loadWarehouseStock,
              ),
            ],
          ),
        ),
        Expanded(
          child: _isLoadingStock
              ? const Center(child: CircularProgressIndicator())
              : _warehouseStock.isEmpty
                  ? Center(
                      child: Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Icon(Icons.inventory_2_outlined, size: 50, color: Colors.grey.shade400),
                          const SizedBox(height: 12),
                          const Text("Belum ada data stok", style: TextStyle(color: Color(0xFF64748B))),
                          const SizedBox(height: 8),
                          ElevatedButton(
                            style: ElevatedButton.styleFrom(backgroundColor: const Color(0xFF0F172A)),
                            onPressed: _loadWarehouseStock,
                            child: const Text("Muat Ulang"),
                          ),
                        ],
                      ),
                    )
                  : ListView.builder(
                      padding: const EdgeInsets.symmetric(horizontal: 16),
                      itemCount: _warehouseStock.length,
                      itemBuilder: (ctx, idx) {
                        final item = _warehouseStock[idx];
                        final isAman = item.status.toUpperCase() == "AMAN";
                        return Container(
                          margin: const EdgeInsets.only(bottom: 10),
                          padding: const EdgeInsets.all(16),
                          decoration: BoxDecoration(
                            color: Colors.white,
                            borderRadius: BorderRadius.circular(16),
                            border: Border.all(color: const Color(0xFFE2E8F0)),
                          ),
                          child: Row(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: [
                              Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Text(item.namaBahan, style: const TextStyle(fontSize: 15, fontWeight: FontWeight.w700)),
                                  const SizedBox(height: 2),
                                  Text(item.kategori, style: const TextStyle(fontSize: 12, color: Color(0xFF64748B))),
                                ],
                              ),
                              Column(
                                crossAxisAlignment: CrossAxisAlignment.end,
                                children: [
                                  Text("${item.stokTersedia.toStringAsFixed(2)} kg", style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w800)),
                                  const SizedBox(height: 2),
                                  Container(
                                    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                                    decoration: BoxDecoration(
                                      color: isAman ? const Color(0xFFECFDF5) : const Color(0xFFFEF2F2),
                                      borderRadius: BorderRadius.circular(10),
                                    ),
                                    child: Text(
                                      item.status,
                                      style: TextStyle(
                                        fontSize: 10,
                                        fontWeight: FontWeight.bold,
                                        color: isAman ? const Color(0xFF059669) : const Color(0xFFDC2626),
                                      ),
                                    ),
                                  ),
                                ],
                              ),
                            ],
                          ),
                        );
                      },
                    ),
        ),
      ],
    );
  }

  // TAB 4: RIWAYAT LOG
  Widget _buildHistoryTab() {
    return Column(
      children: [
        Padding(
          padding: const EdgeInsets.all(16.0),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              const Text("Riwayat Timbangan", style: TextStyle(fontSize: 16, fontWeight: FontWeight.w700)),
              IconButton(
                icon: const Icon(Icons.refresh, color: Color(0xFF0F172A)),
                onPressed: _loadHistory,
              ),
            ],
          ),
        ),
        Expanded(
          child: _isLoadingHistory
              ? const Center(child: CircularProgressIndicator())
              : _historyLogs.isEmpty
                  ? Center(
                      child: Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Icon(Icons.history_outlined, size: 50, color: Colors.grey.shade400),
                          const SizedBox(height: 12),
                          const Text("Belum ada riwayat timbangan", style: TextStyle(color: Color(0xFF64748B))),
                        ],
                      ),
                    )
                  : ListView.builder(
                      padding: const EdgeInsets.symmetric(horizontal: 16),
                      itemCount: _historyLogs.length,
                      itemBuilder: (ctx, idx) {
                        final log = _historyLogs[idx];
                        return Container(
                          margin: const EdgeInsets.only(bottom: 10),
                          padding: const EdgeInsets.all(16),
                          decoration: BoxDecoration(
                            color: Colors.white,
                            borderRadius: BorderRadius.circular(16),
                            border: Border.all(color: const Color(0xFFE2E8F0)),
                          ),
                          child: Row(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: [
                              Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Text(log['item'] ?? '', style: const TextStyle(fontSize: 15, fontWeight: FontWeight.w700)),
                                  const SizedBox(height: 2),
                                  Text("${log['tim_kerja']} • ${log['tanggal']}", style: const TextStyle(fontSize: 12, color: Color(0xFF64748B))),
                                ],
                              ),
                              Text(
                                "${NumberFormat('0.00').format(log['total_berat'] ?? 0)} kg",
                                style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w800, color: Color(0xFF059669)),
                              ),
                            ],
                          ),
                        );
                      },
                    ),
        ),
      ],
    );
  }
}
