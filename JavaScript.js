/**
 * GOOGLE APPS SCRIPT - MBG SPPG KEDUNGWUNI PEKAJANGAN 4
 * Terintegrasi penuh dengan 5 Tab Harian:
 * - "Senin", "Selasa", "Rabu", "Kamis", "Jumat"
 * - "Master Template", "Menu_Mingguan", "Log_Timbangan", "Stok_Gudang"
 */

var SPREADSHEET_ID = "13EctW99CUaaYbx59IZoSh9aJKdRagrZk4kH-0AM1sIM";

function getTargetSpreadsheet() {
  try {
    var active = SpreadsheetApp.getActiveSpreadsheet();
    if (active) return active;
  } catch (err) {}
  return SpreadsheetApp.openById(SPREADSHEET_ID);
}

/**
 * Handle POST Request (Sinkronisasi dari Aplikasi Android / Preview)
 */
function doPost(e) {
  try {
    var ss = getTargetSpreadsheet();
    var data = JSON.parse(e.postData.contents);
    
    // Tentukan Nama Hari (Senin, Selasa, Rabu, Kamis, Jumat)
    var dayName = (data.hari || "").trim();
    if (!dayName) {
      var days = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"];
      var todayIdx = new Date().getDay();
      dayName = days[todayIdx] || "Senin";
      if (dayName === "Sabtu" || dayName === "Minggu") dayName = "Senin";
    }

    // Ambil sheet target harian (misal: "Senin", "Selasa", dst)
    var targetSheet = ss.getSheetByName(dayName);
    if (!targetSheet) {
      targetSheet = ss.getSheetByName("Master Template") || ss.getSheets()[0];
    }

    // Ambil sheet Log_Timbangan untuk audit trail
    var logSheet = ss.getSheetByName("Log_Timbangan");
    if (!logSheet) {
      logSheet = ss.insertSheet("Log_Timbangan");
      logSheet.appendRow([
        "Waktu Server", "Hari", "Tanggal Log", "Waktu", "Tim Kerja / Stasiun",
        "Kategori", "Item Bahan Baku", "Tahapan Alur", "Netto (kg)", "Bruto (kg)",
        "Tara (kg)", "Catatan", "Petugas / Chef"
      ]);
      logSheet.getRange(1, 1, 1, 13).setFontWeight("bold").setBackground("#0F172A").setFontColor("#FFFFFF");
      logSheet.setFrozenRows(1);
    }

    var itemsToProcess = [];
    if (data.batches && Array.isArray(data.batches)) {
      itemsToProcess = data.batches;
    } else if (data.batchItems && Array.isArray(data.batchItems)) {
      itemsToProcess = data.batchItems;
    } else if (data.batch_sessions && Array.isArray(data.batch_sessions)) {
      itemsToProcess = data.batch_sessions;
    } else {
      itemsToProcess = [data];
    }

    var updatedCount = 0;
    for (var idx = 0; idx < itemsToProcess.length; idx++) {
      var itemData = itemsToProcess[idx];
      var itemName = (itemData.item || itemData.itemMenu || itemData.nama_bahan || "").trim();
      if (!itemName) continue;

      var kategori = (itemData.kategori || "Bahan Baku").trim();
      var timKerja = (itemData.tim_kerja || itemData.timKerja || data.team_name || "TIM PERSIAPAN").trim();
      var tahapan = (itemData.tahapan || "").trim();
      var netto = Number(itemData.total_berat || itemData.totalNetWeight || itemData.netto) || 0;
      var satuan = (itemData.satuan || "kg").trim();
      var catatan = (itemData.catatan || "").trim();
      var petugas = (itemData.petugas || data.petugas || "Chef").trim();

      // 1. Perbarui Baris Bahan di Sheet Harian BGN
      if (targetSheet) {
        updateDailyRowBGN(targetSheet, itemName, kategori, satuan, timKerja, tahapan, netto, catatan, petugas);
      }

      // 2. Catat ke Log_Timbangan
      logSheet.appendRow([
        new Date(),
        dayName,
        itemData.tanggal || new Date().toISOString().slice(0, 10),
        itemData.waktu || new Date().toLocaleTimeString("id-ID"),
        timKerja,
        kategori,
        itemName,
        tahapan,
        netto,
        Number(itemData.total_bruto || itemData.bruto) || 0,
        Number(itemData.total_tara || itemData.tara) || 0,
        catatan,
        petugas
      ]);

      updatedCount++;
    }

    return ContentService.createTextOutput(JSON.stringify({
      "status": "success",
      "message": "Berhasil memperbarui form harian " + dayName,
      "sheet": dayName,
      "items_updated": updatedCount,
      "timestamp": new Date().toISOString()
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({
      "status": "error",
      "message": err.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

/**
 * Pemetaan Timbangan ke Kolom Formulir Harian BGN
 */
function updateDailyRowBGN(sheet, itemName, kategori, satuan, timKerja, tahapan, netto, catatan, petugas) {
  var values = sheet.getRange(1, 1, 35, 15).getValues();
  var targetRow = -1;
  var firstEmptyRow = -1;
  var summaryRow = 25;

  for (var r = 16; r < values.length; r++) {
    var colA = (values[r][0] || "").toString().trim().toUpperCase();
    if (colA.indexOf("RINGKASAN") !== -1) {
      summaryRow = r + 1;
      break;
    }
  }

  // Cari baris bahan yang cocok
  for (var i = 16; i < (summaryRow - 1); i++) {
    var existingItem = (values[i][2] || "").toString().trim().toLowerCase();
    if (existingItem === itemName.toLowerCase() || existingItem.indexOf(itemName.toLowerCase()) !== -1 || itemName.toLowerCase().indexOf(existingItem) !== -1) {
      targetRow = i + 1;
      break;
    }
    if (firstEmptyRow === -1 && existingItem === "") {
      firstEmptyRow = i + 1;
    }
  }

  // Jika belum ada di 7 baris, gunakan baris kosong atau tambahkan
  if (targetRow === -1) {
    if (firstEmptyRow !== -1) {
      targetRow = firstEmptyRow;
      sheet.getRange(targetRow, 2).setValue(kategori);
      sheet.getRange(targetRow, 3).setValue(itemName);
      sheet.getRange(targetRow, 4).setValue(satuan || "kg");
    } else {
      targetRow = summaryRow;
      sheet.insertRowBefore(summaryRow);
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

  // ROUTING KE 4 TAHAP:
  if (tk.indexOf("penerimaan") !== -1 || th.indexOf("datang") !== -1 || tk.indexOf("aslap") !== -1) {
    // 1. ASLAP / Barang Datang -> Kolom E (5)
    sheet.getRange(targetRow, 5).setValue(netto);
  } else if (tk.indexOf("persiapan") !== -1 || th.indexOf("sortir") !== -1 || th.indexOf("persiapan") !== -1) {
    // 2. TIM PERSIAPAN -> Kolom F (6)
    sheet.getRange(targetRow, 6).setValue(netto);
  } else if (tk.indexOf("pengolahan") !== -1 || th.indexOf("masak") !== -1 || th.indexOf("produksi") !== -1) {
    // 3. TIM PENGOLAHAN -> Kolom I (9)
    sheet.getRange(targetRow, 9).setValue(netto);
  } else if (tk.indexOf("pemorsian") !== -1 || th.indexOf("porsi") !== -1 || th.indexOf("sisa") !== -1) {
    // 4. TIM PEMORSIAN -> Kolom L (12)
    sheet.getRange(targetRow, 12).setValue(netto);
  } else {
    sheet.getRange(targetRow, 6).setValue(netto);
  }

  if (catatan) {
    var existingKet = sheet.getRange(targetRow, 14).getValue() || "";
    var newKet = existingKet ? (existingKet + " | " + catatan) : catatan;
    sheet.getRange(targetRow, 14).setValue(newKet);
  }

  sheet.getRange(targetRow, 15).setValue(petugas || "✓");
}

/**
 * Handle GET Request (Ambil Menu Mingguan atau Cek Status)
 */
function doGet(e) {
  try {
    var ss = getTargetSpreadsheet();
    var action = (e && e.parameter && e.parameter.action) ? e.parameter.action : "info";

    if (action === "getWeeklyMenu" || action === "menu") {
      var menuSheet = ss.getSheetByName("Menu_Mingguan");
      var menuList = [];
      if (menuSheet) {
        var menuData = menuSheet.getDataRange().getValues();
        for (var m = 1; m < menuData.length; m++) {
          if (!menuData[m][0]) continue;
          menuList.push({
            "hari": menuData[m][0],
            "nama_menu": menuData[m][1],
            "kategori": menuData[m][2],
            "bahan": menuData[m][3],
            "standar_porsi": menuData[m][4],
            "target_porsi": menuData[m][5],
            "arahan_persiapan": menuData[m][6],
            "arahan_pengolahan": menuData[m][7],
            "arahan_pemorsian": menuData[m][8],
            "catatan_gizi": menuData[m][9]
          });
        }
      }
      return ContentService.createTextOutput(JSON.stringify({
        "status": "success",
        "sppg": "SPPG Kedungwuni Pekajangan 4",
        "total_menu": menuList.length,
        "menus": menuList
      })).setMimeType(ContentService.MimeType.JSON);
    }

    return ContentService.createTextOutput(JSON.stringify({
      "status": "success",
      "sppg": "SPPG Kedungwuni Pekajangan 4",
      "sheets": ss.getSheets().map(function(s) { return s.getName(); }),
      "timestamp": new Date().toISOString()
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({
      "status": "error",
      "message": err.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}
