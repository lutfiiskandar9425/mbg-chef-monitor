# MBG Kitchen Monitor & Manajemen Stok Gudang (SPPG Pekajangan)

Aplikasi mobile berbasis **Flutter** yang dirancang khusus untuk memonitor alur bahan baku dan kartu stok gudang program **Makan Bergizi Gratis (MBG)** di Sentra Pelayanan Pemenuhan Gizi (SPPG). 

Aplikasi ini menggunakan teknologi **Google ML Kit Text Recognition** yang di-tuning khusus untuk membaca display timbangan digital **7-Segment LED / LCD**, mendukung penimbangan berulang (**Multi-Batch Camera Uploads**), memiliki penghitung berat otomatis (**Live Total Accumulator**), dan kartu stok gudang otomatis (**Live Inventory Ledger**) yang terintegrasi langsung dengan **Google Sheets Webhook**.

---

## Alur 4 Tahapan Gudang & Dapur MBG

1. **Penerimaan (Datang ke Gudang)**:
   - Menimbang komoditas datang dari supplier / PO (Bumbu, Beras, Sayur, Daging).
   - Menambah angka **Total Masuk Gudang (+)** pada Kartu Stok.
2. **Pengeluaran (Gudang ke Dapur Masak)**:
   - Menimbang bahan dan bumbu yang dikeluarkan untuk porsi menu hari ini.
   - Mengurangi stok tersedia melalui kolom **Keluar ke Dapur (-)**.
3. **Sisa Olahan (Kembali ke Gudang / Next Menu)**:
   - Sesuai arahan Mas Lutfi: jika ada bahan/bumbu yang tersisa saat memasak, bahan tersebut **tidak dibuang**, melainkan ditimbang dan dikembalikan ke gudang.
   - Otomatis menambah angka **Sisa Balik ke Gudang (+)** sebagai persediaan yang siap dipakai pada menu berikutnya.
4. **Limbah & Susut (Waste Non-Reusable)**:
   - Menimbang sisa kupasan atau trimming yang tidak dapat dikonsumsi untuk perhitungan persentase penyusutan (susut bahan).

---

## Integrasi Spreadsheet (Dua Tab Otomatis)

1. **Tab `Log_Timbangan`**:
   - Buku besar pencatatan setiap sesi penimbangan (Waktu, Petugas, Item, Kategori, Tahapan, Total Netto, Bruto, Tara, dan Rincian Wadah).
2. **Tab `Stok_Gudang`**:
   - Kartu stok otomatis dengan formula:
     `Stok Tersedia Saat Ini = (Total Masuk + Sisa Balik ke Gudang) - Keluar ke Dapur`
   - Dilengkapi status stok otomatis: **Tersedia**, **Menipis** (< 5 kg), atau **Habis** (<= 0 kg).
   - Aplikasi Flutter dapat langsung membaca stok ini secara real-time via tab **Stok Gudang**.

---

## Struktur Folder Proyek

```
mbg_chef_monitor/
├── pubspec.yaml
├── README.md
├── build_apk.bat
├── .github/
│   └── workflows/
│       └── build_apk.yml
├── backend/
│   └── google_apps_script.js
├── android/
│   ├── app/
│   │   ├── build.gradle
│   │   └── src/main/
│   │       ├── AndroidManifest.xml
│   │       └── kotlin/com/mbg/sppg/mbg_chef_monitor/MainActivity.kt
│   ├── build.gradle
│   ├── settings.gradle
│   └── gradle.properties
└── lib/
    ├── main.dart
    ├── models/
    │   └── weigh_batch.dart
    ├── services/
    │   ├── ocr_service.dart
    │   └── sheets_service.dart
    └── screens/
        ├── home_screen.dart
        ├── camera_batch_screen.dart
        └── review_sync_screen.dart
```

---

## Panduan Membangun APK (Build APK)

### Opsi 1: Otomatis via GitHub Actions (Rekomendasi - Cepat & Praktis)
1. Push folder `APlikasi MBG` ini ke repository GitHub Anda.
2. Buka tab **Actions** di GitHub repository Anda.
3. Alur kerja **Build Android APK** akan berjalan otomatis dalam 3-4 menit.
4. Unduh file `app-release.apk` langsung dari bagian **Artifacts** di halaman workflow yang selesai.

### Opsi 2: Build di Komputer Lokal
Jika Anda telah memasang Flutter SDK dan Android Studio / SDK:
1. Masuk ke direktori `mbg_chef_monitor`:
   ```bash
   cd "C:\Users\HP\Projects\APlikasi MBG\mbg_chef_monitor"
   ```
2. Jalankan script build otomatis:
   ```cmd
   build_apk.bat
   ```
   Atau perintah manual:
   ```bash
   flutter pub get
   flutter build apk --release
   ```
3. File APK yang dihasilkan akan berada di:
   `build/app/outputs/flutter-apk/app-release.apk`

---

## Setup Google Apps Script (Webhook)

1. Buka Google Sheets tempat rekap timbangan MBG SPPG Anda.
2. Klik menu **Extensions > Apps Script**.
3. Hapus kode default, lalu tempel kode dari file `backend/google_apps_script.js`.
4. Klik tombol **Deploy > New deployment**.
5. Pilih type **Web app**:
   - Description: `MBG Kitchen & Stok Gudang Webhook`
   - Execute as: `Me (email Anda)`
   - Who has access: `Anyone` (Penting agar aplikasi Flutter dapat mengirim dan mengambil data tanpa login akun Google di HP).
6. Salin **Web app URL** yang dihasilkan.
7. Di aplikasi MBG Kitchen Monitor pada HP, buka icon roda gigi (Pengaturan) di kanan atas, lalu tempel URL tersebut.
