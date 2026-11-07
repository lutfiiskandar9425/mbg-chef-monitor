"""
Script untuk membedah dan menata 5 sheet harian (Senin - Jumat)
pada template resmi BGN dengan tanggal otomatis dan menu harian terisi.
"""
import openpyxl
from copy import copy

wb = openpyxl.load_workbook('live_monitoring.xlsx')
template = wb['Monitoring Alur Bahan Baku']

days_config = [
    {
        "name": "Senin",
        "date_str": "Senin, 09 November 2026",
        "menu_str": "Nasi Putih + Daging Ayam Semur Kecap + Tahu Goreng Gurih + Tumis Buncis Jagung Manis + Pisang Cavendish",
        "items": [
            ("Protein Hewani", "Daging Ayam Fillet", "kg"),
            ("Protein Nabati", "Tahu Putih Segar", "kg"),
            ("Sayuran", "Buncis & Jagung Manis", "kg"),
            ("Buah", "Pisang Cavendish", "pcs"),
            ("Karbohidrat", "Beras Putih Premium", "kg"),
            ("Bumbu", "Bumbu Rempah Semur", "kg"),
            ("Bumbu", "Minyak Goreng Sawit", "kg")
        ]
    },
    {
        "name": "Selasa",
        "date_str": "Selasa, 10 November 2026",
        "menu_str": "Nasi Putih + Daging Sapi Teriyaki Lada Hitam + Tempe Goreng Tepung + Capcay Sayur Segar + Jeruk Manis",
        "items": [
            ("Protein Hewani", "Daging Sapi Slice", "kg"),
            ("Protein Nabati", "Tempe Kedelai Murni", "kg"),
            ("Sayuran", "Capcay Sayur Segar", "kg"),
            ("Buah", "Jeruk Manis Medan", "pcs"),
            ("Karbohidrat", "Beras Putih Premium", "kg"),
            ("Bumbu", "Saus Teriyaki & Lada Hitam", "kg"),
            ("Bumbu", "Minyak Goreng Sawit", "kg")
        ]
    },
    {
        "name": "Rabu",
        "date_str": "Rabu, 11 November 2026",
        "menu_str": "Nasi Putih + Ikan Kembung Asam Manis + Tempe Mendoan + Sayur Bayam Jagung Bening + Semangka Merah",
        "items": [
            ("Protein Hewani", "Ikan Kembung Fillet", "kg"),
            ("Protein Nabati", "Tempe Mendoan", "kg"),
            ("Sayuran", "Sayur Bayam & Jagung Manis", "kg"),
            ("Buah", "Semangka Merah Segar", "kg"),
            ("Karbohidrat", "Beras Putih Premium", "kg"),
            ("Bumbu", "Bumbu Asam Manis Nanas", "kg"),
            ("Bumbu", "Minyak Goreng Sawit", "kg")
        ]
    },
    {
        "name": "Kamis",
        "date_str": "Kamis, 12 November 2026",
        "menu_str": "Nasi Putih + Ayam Panggang Bumbu Madu + Rolade Tahu Telur + Sayur Labu Siam Wortel Gurih + Melon Cantaloupe",
        "items": [
            ("Protein Hewani", "Ayam Panggang Madu", "kg"),
            ("Protein Nabati", "Rolade Tahu Telur", "kg"),
            ("Sayuran", "Labu Siam & Wortel", "kg"),
            ("Buah", "Melon Cantaloupe", "kg"),
            ("Karbohidrat", "Beras Putih Premium", "kg"),
            ("Bumbu", "Madu & Bumbu Oles", "kg"),
            ("Bumbu", "Minyak Goreng Sawit", "kg")
        ]
    },
    {
        "name": "Jumat",
        "date_str": "Jumat, 13 November 2026",
        "menu_str": "Nasi Putih + Telur Balado Pedas Manis + Perkedel Kentang Daging + Sayur Lodeh Labu + Pepaya California",
        "items": [
            ("Protein Hewani", "Telur Ayam Balado", "butir"),
            ("Protein Nabati", "Perkedel Kentang Daging", "kg"),
            ("Sayuran", "Sayur Lodeh Labu Siam", "kg"),
            ("Buah", "Pepaya California", "kg"),
            ("Karbohidrat", "Beras Putih Premium", "kg"),
            ("Bumbu", "Bumbu Sambal Balado Manis", "kg"),
            ("Bumbu", "Minyak Goreng Sawit", "kg")
        ]
    }
]

print("Menyiapkan 5 sheet harian...")

