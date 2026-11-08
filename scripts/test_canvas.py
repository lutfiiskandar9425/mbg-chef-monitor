# -*- coding: utf-8 -*-
# Test generating sample scale image
import base64

sample_scale_code = """
function generateSampleScalePhoto(weightStr) {
  const canvas = document.createElement('canvas');
  canvas.width = 640;
  canvas.height = 480;
  const ctx = canvas.getContext('2d');

  // Background timbangan industrial
  ctx.fillStyle = '#0f172a';
  ctx.fillRect(0, 0, 640, 480);

  // Bingkai indikator timbangan digital
  ctx.fillStyle = '#1e293b';
  ctx.strokeStyle = '#334155';
  ctx.lineWidth = 6;
  ctx.beginPath();
  ctx.roundRect(40, 40, 560, 400, 24);
  ctx.fill();
  ctx.stroke();

  // Layar display LED hijau
  ctx.fillStyle = '#022c22';
  ctx.strokeStyle = '#059669';
  ctx.lineWidth = 3;
  ctx.beginPath();
  ctx.roundRect(70, 100, 500, 200, 16);
  ctx.fill();
  ctx.stroke();

  // Header teks
  ctx.fillStyle = '#94a3b8';
  ctx.font = 'bold 16px monospace';
  ctx.fillText('SPPG PEKAJANGAN 04 - DIGITAL SCALE BENCH', 80, 80);

  // Angka timbangan LED
  ctx.fillStyle = '#34d399';
  ctx.font = '900 84px monospace';
  ctx.textAlign = 'right';
  ctx.fillText(weightStr || '25.00', 440, 230);

  ctx.font = 'bold 36px monospace';
  ctx.fillStyle = '#6ee7b7';
  ctx.fillText('kg', 510, 230);

  // Status indikator
  ctx.textAlign = 'left';
  ctx.font = 'bold 14px sans-serif';
  ctx.fillStyle = '#10b981';
  ctx.fillText('● STABIL / NETTO BERSAMA WADAH', 90, 275);

  // Timestamp
  ctx.fillStyle = '#64748b';
  ctx.font = '13px monospace';
  const now = new Date();
  ctx.fillText('TANGGAL: ' + now.toLocaleDateString('id-ID') + ' ' + now.toLocaleTimeString('id-ID') + ' WIB', 70, 360);
  ctx.fillText('STATUS QC: TERVERIFIKASI TIMBANGAN DIGITAL SPPG', 70, 385);

  return canvas.toDataURL('image/jpeg', 0.88);
}
"""
print("Sample scale generator defined.")

