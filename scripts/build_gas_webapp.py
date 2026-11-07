"""
Build Google Apps Script with Embedded Web Monitor (doGet + doPost)
"""
import json

with open('preview.html', 'r', encoding='utf-8') as f:
    html_page = f.read()

# Escape backticks and backslashes for JS template literal
escaped_html = html_page.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')

gas_code = f'''/**
 * GOOGLE APPS SCRIPT - MBG SPPG KEDUNGWUNI PEKAJANGAN 4
 * Terintegrasi penuh:
 * 1. doGet(e): Menampilkan Web Monitor Interaktif (Bebas Layar Putih)
 * 2. doPost(e): Menerima Sinkronisasi Data Timbangan Masuk ke 5 Sheet Harian
 */

var SPREADSHEET_ID = "13EctW99CUaaYbx59IZoSh9aJKdRagrZk4kH-0AM1sIM";

function getTargetSpreadsheet() {{
  try {{
    var active = SpreadsheetApp.getActiveSpreadsheet();
    if (active) return active;
  }} catch (err) {{}}
  return SpreadsheetApp.openById(SPREADSHEET_ID);
}}

/**
 * Handle GET Request: Menampilkan Aplikasi Web Monitor Langsung di Browser HP / Komputer
 */
function doGet(e) {{
  var action = (e && e.parameter && e.parameter.action) ? e.parameter.action : "";

  // Jika memanggil API Menu dalam format JSON
  if (action === "menu" || action === "getWeeklyMenu") {{
    try {{
      var ss = getTargetSpreadsheet();
      var menuSheet = ss.getSheetByName("Menu_Mingguan");
      var menuList = [];
      if (menuSheet) {{
        var data = menuSheet.getDataRange().getValues();
        for (var m = 1; m < data.length; m++) {{
          if (!data[m][0]) continue;
          menuList.push({{
            periode: data[m][0],
            hari: data[m][1],
            komponen: data[m][2],
            bahan: data[m][3],
            resep: data[m][4],
            target: data[m][5],
            stasiun: data[m][6]
          }});
        }}
      }}
      return ContentService.createTextOutput(JSON.stringify({{ status: "success", data: menuList }}))
        .setMimeType(ContentService.MimeType.JSON);
    }} catch (err) {{
      return ContentService.createTextOutput(JSON.stringify({{ status: "error", message: err.toString() }}))
        .setMimeType(ContentService.MimeType.JSON);
    }}
  }}

  // Tampilkan Web App MBG Kitchen Monitor secara instan di browser
  var htmlOutput = HtmlService.createHtmlOutput(getEmbeddedAppHtml())
    .setTitle("MBG Chef & ASLAP Monitor - SPPG Kedungwuni Pekajangan 4")
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL)
    .addMetaTag('viewport', 'width=device-width, initial-scale=1');

  return htmlOutput;
}}

/**
 * Handle POST Request: Sinkronisasi Data Timbangan Masuk ke Sheet Harian
 */
function doPost(e) {{
  try {{
    var ss = getTargetSpreadsheet();
    var data = JSON.parse(e.postData.contents);
    
    var dayName = (data.hari || "").trim();
    if (!dayName) {{
      var days = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"];
      var todayIdx = new Date().getDay();
      dayName = days[todayIdx] || "Senin";
      if (dayName === "Sabtu" || dayName === "Minggu") dayName = "Senin";
    }}

    var targetSheet = ss.getSheetByName(dayName);
    if (!targetSheet) {{
      targetSheet = ss.getSheetByName("Master Template") || ss.getSheets()[0];
    }}

    var logSheet = ss.getSheetByName("Log_Timbangan");
    if (!logSheet) {{
      logSheet = ss.insertSheet("Log_Timbangan");
      logSheet.appendRow([
        "Waktu Server", "Hari", "Tanggal Log", "Waktu", "Tim Kerja / Stasiun",
        "Kategori", "Item Bahan Baku", "Tahapan Alur", "Netto (kg)", "Bruto (kg)",
        "Tara (kg)", "Catatan", "Petugas / Chef"
      ]);
      logSheet.getRange(1, 1, 1, 13).setFontWeight("bold").setBackground("#0F172A").setFontColor("#FFFFFF");
    }}

    var now = new Date();
    var serverTimestamp = Utilities.formatDate(now, "Asia/Jakarta", "yyyy-MM-dd HH:mm:ss");

    var items = data.items || [data];
    var insertedCount = 0;

    for (var i = 0; i < items.length; i++) {{
      var item = items[i];
      var netto = parseFloat(item.netto || item.total_net_weight || 0);
      var bruto = parseFloat(item.bruto || item.total_gross_weight || 0);
      var tara = parseFloat(item.tara || item.total_tare_weight || 0);
      var itemName = item.name || item.item_menu || "Bahan Baku";
      var team = item.team || item.tim_kerja || "TIM PERSIAPAN";
      var category = item.category || item.kategori || "Umum";
      var tahapan = item.tahapan || "Penerimaan";
      var catatan = item.catatan || "";
      var petugas = item.petugas || "Petugas Dapur";

      logSheet.appendRow([
        serverTimestamp, dayName, Utilities.formatDate(now, "Asia/Jakarta", "yyyy-MM-dd"),
        Utilities.formatDate(now, "Asia/Jakarta", "HH:mm:ss"), team, category,
        itemName, tahapan, netto, bruto, tara, catatan, petugas
      ]);

      insertedCount++;
    }}

    return ContentService.createTextOutput(JSON.stringify({{
      status: "success",
      message: "Berhasil mencatat " + insertedCount + " item ke sheet " + dayName,
      timestamp: serverTimestamp
    }})).setMimeType(ContentService.MimeType.JSON);

  }} catch (error) {{
    return ContentService.createTextOutput(JSON.stringify({{
      status: "error",
      message: error.toString()
    }})).setMimeType(ContentService.MimeType.JSON);
  }}
}}

/**
 * Return Embedded HTML Application Code
 */
function getEmbeddedAppHtml() {{
  return `{escaped_html}`;
}}
'''

with open('backend/google_apps_script.js', 'w', encoding='utf-8') as f:
    f.write(gas_code)

print("backend/google_apps_script.js berhasil dibuat dengan Web App terpadu!")

