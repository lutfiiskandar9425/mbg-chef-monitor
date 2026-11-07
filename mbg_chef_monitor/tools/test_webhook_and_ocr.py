"""
Helper Script MBG Kitchen Monitor
Menggunakan Embedded Python Environment di C:\\Users\\HP\\Projects\\Projecttools
"""

import sys
import json
import urllib.request
import re

def test_google_sheets_webhook(webhook_url):
    print("==================================================")
    print(" Menguji Koneksi Webhook Google Sheets SPPG...")
    print("==================================================")
    
    if not webhook_url or "YOUR_SCRIPT_ID" in webhook_url:
        print("[INFO] Webhook URL masih default atau belum diisi.")
        return False

    sample_payload = {
        "tim_kerja": "TIM PERSIAPAN",
        "tanggal": "2026-11-03",
        "waktu": "18:30:00",
        "kategori": "Bumbu & Bahan Kering",
        "item": "Bawang Merah Kupas (Uji Python)",
        "tahapan": "Penerimaan (Datang ke Gudang)",
        "total_berat": 12.50,
        "total_bruto": 13.35,
        "total_tara": 0.85,
        "jumlah_wadah": 1,
        "batch_detail": [12.50],
        "catatan": "Pengujian otomatis dari Python Projecttools",
        "petugas": "Head Chef Lutfi"
    }

    try:
        req = urllib.request.Request(
            webhook_url,
            data=json.dumps(sample_payload).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read().decode('utf-8')
            print(f"[STATUS] HTTP {resp.status}")
            print(f"[RESPON] {data}")
            return True
    except Exception as e:
        print(f"[GAGAL] Error saat menghubungi webhook: {e}")
        return False

def test_7segment_ocr_normalizer(raw_text):
    print("==================================================")
    print(f" Menguji Normalisasi Karakter 7-Segment LED: '{raw_text}'")
    print("==================================================")
    
    clean = raw_text.upper()
    keywords = ['NET', 'GROSS', 'TARE', 'STABLE', 'ZERO', 'HOLD', 'KG']
    for kw in keywords:
        clean = clean.replace(kw, ' ')
    
    # Substitusi karakter rancu LED
    char_map = {
        'S': '5', 'O': '0', 'D': '0', 'Q': '0',
        'I': '1', 'L': '1', '|': '1', '!': '1', '/': '1',
        'B': '8', 'Z': '2', 'A': '4', 'T': '7', 'G': '6'
    }
    
    normalized = list(clean)
    for i, ch in enumerate(normalized):
        if ch in char_map:
            normalized[i] = char_map[ch]
    normalized_str = "".join(normalized)
    
    # Ambil angka desimal
    match = re.search(r'\b\d{1,3}[\.,:]\d{2}\b', normalized_str)
    if match:
        val = match.group(0).replace(',', '.').replace(':', '.')
        print(f"[HASIL] Angka berat valid terdeteksi: {val} kg")
        return float(val)
    else:
        print("[INFO] Tidak ditemukan pola desimal standar, mencoba pola bulat...")
        return None

if __name__ == '__main__':
    print("Python Interpreter:", sys.executable)
    # Test OCR logic
    test_7segment_ocr_normalizer("STABLE 1S.80 KG")
    test_7segment_ocr_normalizer("NET 73:16")
    test_7segment_ocr_normalizer("TARE 0.85 kg")

