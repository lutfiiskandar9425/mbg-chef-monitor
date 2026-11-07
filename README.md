# MBG Chef Monitor — SPPG Kedungwuni Pekajangan 4
**Yayasan Maranatha Cita Kasih • Badan Gizi Nasional Republik Indonesia**

Aplikasi mobile Android resmi untuk Head Chef dan Tim Quality Control (QC) Satuan Pelayanan Pemenuhan Gizi (SPPG) dalam mencatat, menimbang, dan memantau seluruh alur bahan baku produksi secara otomatis dengan integrasi langsung ke Google Sheets resmi Badan Gizi Nasional.

---

## Arsitektur Sistem & Alur Kerja

```
[ Timbangan Digital Dapur ]
           │
           ▼
[ MBG Chef Monitor (Android APK) ]
   ├── Foto Kamera Langsung / Ambil dari Galeri
   ├── Deteksi Angka LED Otomatis (Google ML Kit OCR)
   ├── Pengurangan Tara Otomatis (Preset Wadah: 0.85 kg, 0.50 kg, 0.00 kg)
   └── Keranjang Staging Akumulasi per Tim Kerja (Persiapan, Sayur, Buah, Saos, dll.)
           │
           ▼ (HTTPS Webhook JSON)
[ Google Apps Script Backend (Web App) ]
   ├── Validasi Token & Payload
   ├── Rekap Log Detail per Wadah (Tab 'Log_Timbangan')
   ├── Pembaruan Stok Masuk/Keluar/Sisa (Tab 'Stok_Gudang')
   └── Pengisian Otomatis Kolom Resmi BGN (Tab 'Monitoring Alur Bahan Baku')
           │
           ▼
[ Google Spreadsheet Live MBG ]
   ├── E: Barang Datang
   ├── F: Berat Setelah Sortir (Persiapan)
   ├── I: Berat Hasil Produksi (Pengolahan)
   ├── L: Sisa (Pemorsian)
   └── Rumus Otomatis BGN: Susut Sortir, % Susut, dan Total Terporsi
```

---

## Struktur Folder Proyek

```
APlikasi MBG/
├── mbg_chef_monitor/          # Source code aplikasi mobile Flutter
│   ├── lib/                   # Arsitektur Flutter (screens, models, services)
│   ├── android/               # Konfigurasi native Android & mipmap launcher icons
│   ├── assets/images/         # Aset logo resmi BGN di dalam aplikasi
│   └── .github/workflows/     # CI/CD otomatis rakit APK di GitHub Actions
│
├── apk_output/                # Lokasi file APK siap install di HP Android
│   └── app-release.apk        # APK rilis terbaru (dengan logo BGN resmi)
│
├── backend/                   # Backend skrip Google Apps Script
│   └── google_apps_script.js  # Kode master Apps Script (doGet & doPost)
│
├── assets/                    # Aset logo master kualitas tinggi
│   ├── logo_bgn_512.png       # Master PNG transparan 512x512
│   └── bgn_logo_master.png    # Master emblem anti-aliased
│
├── references/                # Dokumen referensi & template resmi
│   └── drive_template.xlsx    # Cadangan template resmi Google Sheet BGN
│
├── scripts/                   # Alat otomatisasi Python (Python 3.11 Projecttools)
│   ├── sync_apk.py            # Sinkronisasi & unduh APK dari rilis GitHub
│   ├── generate_icons.py      # Generator ukuran icon Android (mdpi - xxxhdpi)
│   ├── encode_logo.py         # Encoder Base64 logo untuk preview mandiri
│   ├── test_real_webhook.py   # Penguji kirim data timbangan ke Google Sheet
│   └── inspect_template.py    # Inspeksi sel & formula template Excel/Sheet
│
├── JavaScript.js              # Salinan mirror skrip Google Apps Script
└── README.md                  # Dokumentasi master proyek
```

---

## Panduan Instalasi & Penggunaan

### 1. Unduh & Pasang APK di HP Android
File APK rilis terbaru dapat diunduh langsung melalui:
- **Tautan GitHub Release:**  
  https://github.com/lutfiiskandar888-svg/mbg-chef-monitor/releases/download/v1.0.0/mbg-chef-monitor.apk
- **File Lokal di Laptop:**  
  `C:\Users\HP\Projects\APlikasi MBG\apk_output\app-release.apk`

*Catatan:* Saat pertama kali install dari luar Play Store, izinkan opsi *"Install from Unknown Sources"* pada HP Android.

### 2. Pengaturan Webhook Google Apps Script
1. Buka Google Spreadsheet monitoring SPPG di Google Drive: `Form Monitoring Alur Bahan Baku MBG SPPG (Live)`.
2. Klik menu **Ekstensi** > **Apps Script**.
3. Buka file `Kode.gs`, salin seluruh isi dari file `backend/google_apps_script.js` (atau `JavaScript.js`), lalu tempel dan tekan **Ctrl + S** (Simpan).
4. Klik tombol biru **Terapkan (Deploy)** di kanan atas > **Kelola penerapan**.
5. Klik ikon **Pensil (Edit)** pada web app.
6. Pada bagian **Versi (Version)**, pilih **Versi baru (New version)**.
7. Pastikan **Akses** diset ke **Siapa saja (Anyone)**.
8. Klik **Terapkan**, lalu simpan URL Webhook yang dihasilkan.
9. Di aplikasi Android, klik ikon gear/pengaturan di kanan atas layar utama, lalu tempelkan URL tersebut.

### 3. Fitur Utama di Dapur
- **Pilihan Sumber Foto:** Dapat mengambil foto langsung dengan kamera HP atau memilih foto hasil timbang yang sudah tersimpan di galeri.
- **Pilihan Stasiun Kerja:** Tim Persiapan, Tim Pengolahan (Prohe, Prona, Sayur, Saos & Sambal), Tim Buah & Potong, serta Tim Pemorsian.
- **Preset Wadah:** Opsi cepat pengurangan bobot tara wadah (0.85 kg, 0.50 kg, 0.00 kg) atau input custom.
- **Keranjang Akumulasi (Batch Staging):** Chef dapat menimbang berulang kali per wadah hingga selesai satu menu, lalu mengirimkan akumulasinya sekaligus ke Google Sheet dalam satu ketukan tombol.

