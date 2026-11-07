"""
Script untuk mengekstrak arahan dan menu dari dokumen PDF Mas Lutfi
menggunakan pdfplumber (Python Projecttools) dan menyinkronkannya
ke Google Sheets dan sistem monitoring MBG Pekajangan 04.
"""
import sys
import os
import json
import pdfplumber
import requests

PDF_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "SOP_Menu_Mingguan_SPPG_Pekajangan04.pdf")
WEBHOOK_URL = "https://script.google.com/macros/s/AKfycby08_sY6VmSOS1WbUFpNIDEUS9NthbaTMaeaYYzJuoxaHKAAJUSOieBBlyfYBnBaL2D/exec"

def extract_pdf_menu(pdf_file=PDF_PATH):
    if not os.path.exists(pdf_file):
        print(f"Berkas {pdf_file} tidak ditemukan.")
        return None

    extracted_data = {
        "file_name": os.path.basename(pdf_file),
        "pages": [],
        "teams": {
            "TIM PERSIAPAN": [],
            "TIM PENGOLAHAN": [],
            "TIM PEMORSIAN": []
        }
    }

    with pdfplumber.open(pdf_file) as pdf:
        print(f"Membaca {len(pdf.pages)} halaman PDF dari {pdf_file}...")
        for page_idx, page in enumerate(pdf.pages):
            text = page.extract_text()
            extracted_data["pages"].append({
                "page": page_idx + 1,
                "text": text
            })
            
            # Ekstrak tabel jika ada
            tables = page.extract_tables()
            if tables:
                print(f"Halaman {page_idx + 1}: Ditemukan {len(tables)} tabel.")

    print("Ekstraksi PDF berhasil!")
    return extracted_data

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else PDF_PATH
    res = extract_pdf_menu(target)
    if res:
        print(f"Berhasil mengekstrak {len(res['pages'])} halaman.")

