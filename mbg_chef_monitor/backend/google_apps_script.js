/**
 * GOOGLE APPS SCRIPT - MBG KITCHEN MONITORING SPPG
 * Satuan Pelayanan Pemenuhan Gizi Pekalongan Kedungwuni Pekajangan 4
 * Yayasan Maranatha Cita Kasih
 * 
 * Terintegrasi langsung dengan Formulir Resmi:
 * "FORM MONITORING ALUR BAHAN BAKU PRODUKSI"
 * Serta tab pendukung "Log_Timbangan" & "Stok_Gudang".
 */

var SPREADSHEET_ID = "13EctW99CUaaYbx59IZoSh9aJKdRagrZk4kH-0AM1sIM";

function getTargetSpreadsheet() {
  try {
    var active = SpreadsheetApp.getActiveSpreadsheet();
    if (active) return active;
  } catch (err) {}
  return SpreadsheetApp.openById(SPREADSHEET_ID);
}

function doPost(e) {
  try {
    var ss = getTargetSpreadsheet();
    
    // 1. Dapatkan Sheet Monitoring Utama (Template Resmi BGN)
    var monitorSheet = ss.getSheetByName("Monitoring Alur Bahan Baku") || ss.getSheets()[0];
    
    // 2. Dapatkan atau buat Sheet Log_Timbangan untuk audit foto & transaksi per wadah
    var logSheet = ss.getSheetByName("Log_Timbangan");
    if (!logSheet) {
      logSheet = ss.insertSheet("Log_Timbangan");
      logSheet.appendRow([
        "Waktu Server",
        "Tanggal Log",
        "Waktu",
        "Tim Kerja / Stasiun",
        "Kategori",
        "Item Bahan Baku",
        "Tahapan Alur",
        "Netto (kg)",
        "Bruto (kg)",
        "Tara (kg)",
        "Jumlah Wadah",
        "Rincian Wadah",
        "Catatan",
        "Petugas / Chef"
      ]);
      logSheet.getRange(1, 1, 1, 14).setFontWeight("bold").setBackground("#00695C").setFontColor("#FFFFFF");
      logSheet.setFrozenRows(1);
    }
    
    // 3. Dapatkan atau buat Sheet Stok_Gudang
    var stokSheet = ss.getSheetByName("Stok_Gudang");
    if (!stokSheet) {
      stokSheet = ss.insertSheet("Stok_Gudang");
      stokSheet.appendRow([
        "Kode / Nama Bahan",
        "Kategori",
        "Total Masuk Gudang (kg)",
        "Keluar ke Dapur (kg)",
        "Sisa Balik ke Gudang (kg)",
        "Limbah / Susut (kg)",
        "Stok Tersedia Saat Ini (kg)",
        "Status Stok",
        "Update Terakhir"
      ]);
      stokSheet.getRange(1, 1, 1, 9).setFontWeight("bold").setBackground("#004D40").setFontColor("#FFFFFF");
      stokSheet.setFrozenRows(1);
    }
    
    var data = JSON.parse(e.postData.contents);
    
    // Ekstraksi batch sessions
    var itemsToProcess = [];
    if (data.batch_sessions && Array.isArray(data.batch_sessions)) {
      itemsToProcess = data.batch_sessions;
    } else {
      itemsToProcess = [data];
    }
    
    // Update metadata form jika disertakan (Hari/Tanggal, Menu, Petugas)
    if (monitorSheet) {
      if (data.tanggal) {
        monitorSheet.getRange("D9").setValue(data.tanggal);
      }
      if (data.menu) {
        monitorSheet.getRange("D10").setValue(data.menu);
      }
      if (data.petugas_qc || data.petugas) {
        monitorSheet.getRange("D14").setValue(data.petugas_qc || data.petugas);
      }
    }
    
    var rowCount = 0;
    for (var k = 0; k < itemsToProcess.length; k++) {
      var itemData = itemsToProcess[k];
      var itemName = (itemData.item || "Bahan Baku").trim();
      var timKerja = (itemData.tim_kerja || data.tim_kerja || "Tim Persiapan").trim();
      var kategori = (itemData.kategori || "Umum").trim();
      var tahapan = (itemData.tahapan || "").trim();
      var netto = Number(itemData.total_berat) || 0;
      var satuan = (itemData.satuan || "kg").trim();
      var catatan = (itemData.catatan || "").trim();
      var petugas = (itemData.petugas || data.petugas || "Chef").trim();
      
      // A. Masukkan ke Formulir Resmi BGN "Monitoring Alur Bahan Baku"
      if (monitorSheet) {
        updateFormBGN(monitorSheet, itemName, kategori, satuan, timKerja, tahapan, netto, catatan, petugas);
      }
      
      // B. Catat ke Log_Timbangan untuk audit trail
      logSheet.appendRow([
        new Date(),
        itemData.tanggal || new Date().toISOString().slice(0, 10),
        itemData.waktu || new Date().toLocaleTimeString("id-ID"),
        timKerja,
        kategori,
        itemName,
        tahapan,
        netto,
        Number(itemData.total_bruto) || 0,
        Number(itemData.total_tara) || 0,
        Number(itemData.jumlah_wadah) || 1,
        JSON.stringify(itemData.batch_detail || []),
        catatan,
        petugas
      ]);
      
      // C. Mutasi Stok Gudang
      updateKartuStokGudang(stokSheet, itemName, kategori, tahapan, netto);
      rowCount++;
    }
    
    return ContentService.createTextOutput(JSON.stringify({
      "status": "success",
      "message": "Sukses: " + rowCount + " bahan berhasil dipetakan ke Formulir Alur Bahan Baku BGN.",
      "items_count": rowCount
    })).setMimeType(ContentService.MimeType.JSON);
    
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({
      "status": "error",
      "message": err.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

/**
 * Pemetaan Data ke Formulir BGN "Monitoring Alur Bahan Baku"
 */
function updateFormBGN(sheet, itemName, kategori, satuan, timKerja, tahapan, netto, catatan, petugas) {
  var values = sheet.getRange(1, 1, 40, 15).getValues();
  var targetRow = -1;
  var firstEmptyRow = -1;
  var summaryRow = 25; // Default baris 'RINGKASAN & VERIFIKASI'
  
  for (var r = 16; r < values.length; r++) {
    var colA = (values[r][0] || "").toString().trim().toUpperCase();
    if (colA.indexOf("RINGKASAN") !== -1) {
      summaryRow = r + 1;
      break;
    }
  }
  
  for (var i = 16; i < (summaryRow - 1); i++) {
    var existingItem = (values[i][2] || "").toString().trim().toLowerCase();
    if (existingItem === itemName.toLowerCase()) {
      targetRow = i + 1;
      break;
    }
    if (firstEmptyRow === -1 && existingItem === "") {
      firstEmptyRow = i + 1;
    }
  }
  
  if (targetRow === -1) {
    if (firstEmptyRow !== -1) {
      targetRow = firstEmptyRow;
      sheet.getRange(targetRow, 2).setValue(kategori);
      sheet.getRange(targetRow, 3).setValue(itemName);
      sheet.getRange(targetRow, 4).setValue(satuan || "kg");
    } else {
      sheet.insertRowBefore(summaryRow);
      targetRow = summaryRow;
      var itemNum = targetRow - 16;
      sheet.getRange(targetRow, 1).setValue(itemNum);
      sheet.getRange(targetRow, 2).setValue(kategori);
      sheet.getRange(targetRow, 3).setValue(itemName);
      sheet.getRange(targetRow, 4).setValue(satuan || "kg");
      
      sheet.getRange(targetRow, 7).setFormula('=IFERROR(E' + targetRow + '-F' + targetRow + ',"")');
      sheet.getRange(targetRow, 8).setFormula('=IFERROR(G' + targetRow + '/E' + targetRow + ',"")');
      sheet.getRange(targetRow, 10).setFormula('=IFERROR(F' + targetRow + '-I' + targetRow + ',"")');
      sheet.getRange(targetRow, 11).setFormula('=IFERROR(J' + targetRow + '/F' + targetRow + ',"")');
      sheet.getRange(targetRow, 13).setFormula('=IFERROR(I' + targetRow + '-L' + targetRow + ',"")');
    }
  }
  
  var tk = timKerja.toLowerCase();
  var th = tahapan.toLowerCase();
  
  if (tk.indexOf("persiapan") !== -1 || th.indexOf("sortir") !== -1 || th.indexOf("persiapan") !== -1 || (tk.indexOf("buah") !== -1 && th.indexOf("datang") === -1)) {
    // Tim Persiapan atau Tim Buah Potong -> Kolom F (Berat Setelah Sortir / Kupas)
    sheet.getRange(targetRow, 6).setValue(netto);
  } else if (tk.indexOf("pengolahan") !== -1 || th.indexOf("produksi") !== -1 || th.indexOf("masak") !== -1 || tk.indexOf("saos") !== -1 || tk.indexOf("sambal") !== -1) {
    // Tim Pengolahan (Sayur, Prohe, Prona, Saos / Sambal) -> Kolom I (Berat Hasil Produksi)
    sheet.getRange(targetRow, 9).setValue(netto);
  } else if (tk.indexOf("pemorsian") !== -1 || th.indexOf("porsi") !== -1 || th.indexOf("sisa") !== -1) {
    // Tim Pemorsian -> Kolom L (Sisa Pemorsian)
    sheet.getRange(targetRow, 12).setValue(netto);
  } else if (tk.indexOf("penerimaan") !== -1 || th.indexOf("datang") !== -1 || th.indexOf("gudang") !== -1) {
    // Penerimaan Barang Datang -> Kolom E (Barang Datang)
    sheet.getRange(targetRow, 5).setValue(netto);
  } else {
    sheet.getRange(targetRow, 6).setValue(netto);
  }
  
  if (catatan) {
    var oldKet = sheet.getRange(targetRow, 14).getValue() || "";
    var newKet = oldKet ? oldKet + "; " + catatan : catatan;
    sheet.getRange(targetRow, 14).setValue(newKet);
  }
  if (petugas) {
    sheet.getRange(targetRow, 15).setValue(petugas);
  }
}

/**
 * Logika Pengkinian Stok Gudang
 */
function updateKartuStokGudang(sheet, item, kategori, tahapan, netto) {
  var data = sheet.getDataRange().getValues();
  var rowIndex = -1;
  
  for (var i = 1; i < data.length; i++) {
    if (data[i][0].toString().toLowerCase() === item.toLowerCase()) {
      rowIndex = i + 1;
      break;
    }
  }
  
  var now = new Date();
  var timestamp = Utilities.formatDate(now, "Asia/Jakarta", "dd/MM/yyyy HH:mm:ss");
  
  if (rowIndex === -1) {
    var masuk = (tahapan.toLowerCase().indexOf("datang") !== -1 || tahapan.toLowerCase().indexOf("gudang") !== -1) ? netto : 0;
    var keluar = (tahapan.toLowerCase().indexOf("keluar") !== -1 || tahapan.toLowerCase().indexOf("persiapan") !== -1) ? netto : 0;
    var sisa = 0;
    var limbah = 0;
    var stokTersedia = masuk - keluar;
    
    sheet.appendRow([
      item,
      kategori,
      masuk,
      keluar,
      sisa,
      limbah,
      stokTersedia,
      stokTersedia > 5 ? "AMAN" : "MENIPIS",
      timestamp
    ]);
  } else {
    var curMasuk = Number(data[rowIndex - 1][2]) || 0;
    var curKeluar = Number(data[rowIndex - 1][3]) || 0;
    var curSisa = Number(data[rowIndex - 1][4]) || 0;
    var curLimbah = Number(data[rowIndex - 1][5]) || 0;
    
    var th = tahapan.toLowerCase();
    if (th.indexOf("datang") !== -1 || th.indexOf("gudang") !== -1) {
      curMasuk += netto;
    } else if (th.indexOf("keluar") !== -1 || th.indexOf("persiapan") !== -1) {
      curKeluar += netto;
    } else if (th.indexOf("sisa") !== -1 || th.indexOf("balik") !== -1) {
      curSisa += netto;
    } else if (th.indexOf("limbah") !== -1 || th.indexOf("susut") !== -1) {
      curLimbah += netto;
    }
    
    var stokAkhir = curMasuk - curKeluar + curSisa - curLimbah;
    sheet.getRange(rowIndex, 3).setValue(curMasuk);
    sheet.getRange(rowIndex, 4).setValue(curKeluar);
    sheet.getRange(rowIndex, 5).setValue(curSisa);
    sheet.getRange(rowIndex, 6).setValue(curLimbah);
    sheet.getRange(rowIndex, 7).setValue(stokAkhir);
    sheet.getRange(rowIndex, 8).setValue(stokAkhir > 5 ? "AMAN" : "MENIPIS");
    sheet.getRange(rowIndex, 9).setValue(timestamp);
  }
}

/**
 * Tampilan Ramah jika URL dibuka langsung dari Browser (GET Request)
 */
function doGet(e) {
  if (e && e.parameter && e.parameter.format === "json") {
    var ss = getTargetSpreadsheet();
    var stokSheet = ss.getSheetByName("Stok_Gudang");
    var stockList = [];
    if (stokSheet) {
      var data = stokSheet.getDataRange().getValues();
      for (var i = 1; i < data.length; i++) {
        stockList.push({
          "item": data[i][0],
          "kategori": data[i][1],
          "stok_tersedia": data[i][6],
          "status": data[i][7]
        });
      }
    }
    return ContentService.createTextOutput(JSON.stringify({ "status": "success", "stock": stockList }))
      .setMimeType(ContentService.MimeType.JSON);
  }
  
  var html = '<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Webhook MBG Aktif</title>' +
    '<style>' +
    'body { font-family: "Segoe UI", Arial, sans-serif; background: #0A192F; color: #ECEFF1; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }' +
    '.card { background: #112240; padding: 32px 40px; border-radius: 16px; border: 1px solid #00B4D8; box-shadow: 0 10px 30px rgba(0,0,0,0.5); text-align: center; max-width: 500px; }' +
    'h2 { color: #64FFDA; margin-top: 0; }' +
    'p { line-height: 1.6; color: #8892B0; }' +
    '.badge { background: rgba(100, 255, 218, 0.15); color: #64FFDA; padding: 6px 16px; border-radius: 20px; font-weight: bold; display: inline-block; margin-bottom: 16px; }' +
    '</style></head><body>' +
    '<div class="card">' +
    '<div class="badge">STATUS: ONLINE & AKTIF</div>' +
    '<h2>MBG Kitchen Monitoring SPPG</h2>' +
    '<p>Webhook Google Apps Script terhubung sempurna ke <b>Formulir Monitoring Alur Bahan Baku</b> Kedungwuni Pekajangan 4.</p>' +
    '<p style="font-size: 13px; color: #A8B2D1;">URL ini siap menerima data timbangan otomatis dari aplikasi Android MBG Chef Monitor.</p>' +
    '</div></body></html>';
    
  return HtmlService.createHtmlOutput(html).setTitle("Webhook MBG Kitchen Monitor");
}
