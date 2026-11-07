# Panduan Integrasi Google Apps Script MBG SPPG

File `google_apps_script.js` merupakan skrip backend otomatis yang menghubungkan aplikasi Android **MBG Chef Monitor** langsung dengan formulir resmi Badan Gizi Nasional (BGN):
`FORM MONITORING ALUR BAHAN BAKU PRODUKSI`.

---

## Langkah Penerapan (Deploy) di Google Sheets

1. Buka spreadsheet monitoring di browser.
2. Klik menu **Ekstensi (Extensions)** > **Apps Script**.
3. Di tab **Kode.gs**, hapus semua teks yang ada lalu tempelkan seluruh kode dari `google_apps_script.js`.
4. Tekan **Ctrl + S** untuk menyimpan.
5. Jalankan fungsi `doGet` sekali untuk memicu dialog izin OAuth Google:
   - Pilih fungsi `doGet` pada dropdown di samping tombol *Jalankan (Run)*.
   - Klik **Jalankan**.
   - Jika muncul peringatan *"Google hasn't verified this app"*, klik **Advanced** (Lanjutan) di kiri bawah, lalu klik **Go to [Nama Project] (unsafe)**.
   - Klik **Allow** (Izinkan).
6. Klik tombol biru **Terapkan (Deploy)** di pojok kanan atas:
   - Pilih **Kelola penerapan (Manage deployments)** jika sudah pernah dibuat, atau **Penerapan baru (New deployment)**.
   - Jenis penerapan: **Aplikasi Web (Web app)**.
   - Deskripsi: `MBG Kitchen Monitor SPPG`.
   - Jalankan sebagai: **Saya (Akun pemilik)**.
   - Siapa yang memiliki akses: **Siapa saja (Anyone)**.
   - Pada kolom Versi: Pilih **Versi baru (New version)**.
   - Klik **Terapkan**.
7. Salin URL Aplikasi Web yang berakhiran `/exec`.
8. Buka URL tersebut di browser untuk memastikan status: halaman navy gelap dengan teks **STATUS: ONLINE & AKTIF** akan tampil.
9. Masukkan URL tersebut ke menu pengaturan aplikasi Android MBG Chef Monitor.

---

## Fitur Otomatis Skrip
- **doGet(e):** Antarmuka web ramah pengguna untuk mengecek status online dan mengambil data stok gudang dalam format JSON.
- **doPost(e):** Penerima data transaksi timbangan dari aplikasi Android. Menulis data ke baris item terkait di sheet utama, membuat rekaman rinci di sheet `Log_Timbangan`, serta memperbarui kartu stok di sheet `Stok_Gudang`.

