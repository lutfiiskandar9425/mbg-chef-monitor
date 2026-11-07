import urllib.request
import json

url = 'https://script.google.com/macros/s/AKfycby08_sY6VmSOS1WbUFpNIDEUS9NthbaTMaeaYYzJuoxaHKAAJUSOieBBlyfYBnBaL2D/exec'

# 1. Test GET (Stock)
print("Testing GET...")
req_get = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req_get, timeout=20) as resp:
        print("GET Status:", resp.status)
        print("GET Body:", resp.read().decode())
except Exception as e:
    print("GET Error:", e)

# 2. Test POST (Simulated batch item from Tim Persiapan)
print("\nTesting POST (Simulate Tim Persiapan weigh)...")
test_payload = json.dumps({
    "tanggal": "2026-11-04",
    "menu": "Ayam Kecap, Sayur Sop, Tempe Goreng",
    "petugas_qc": "Mas Lutfi",
    "tim_kerja": "Tim Persiapan",
    "batch_sessions": [
        {
            "item": "Wortel",
            "kategori": "Sayuran",
            "satuan": "kg",
            "tahapan": "Persiapan (Sortir)",
            "total_berat": 12.5,
            "total_bruto": 13.5,
            "total_tara": 1.0,
            "jumlah_wadah": 2,
            "catatan": "Wortel kupas segar sortir A",
            "petugas": "Mas Lutfi"
        }
    ]
}).encode('utf-8')

req_post = urllib.request.Request(url, data=test_payload, headers={
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
})

try:
    with urllib.request.urlopen(req_post, timeout=25) as resp:
        print("POST Status:", resp.status)
        print("POST Body:", resp.read().decode())
except Exception as e:
    print("POST Error:", e)

