import openpyxl

wb = openpyxl.load_workbook('live_monitoring.xlsx', data_only=True)

for name in wb.sheetnames:
    ws = wb[name]
    print(f"\n==================== DETAIL SHEET: '{name}' ====================")
    # Check row 9, 10, 12, 13, 14, 15
    for r in range(8, 16):
        vals = [f"{openpyxl.utils.get_column_letter(c)}{r}: '{ws.cell(r, c).value}'" for c in range(1, 16) if ws.cell(r, c).value is not None]
        if vals:
            print(f"Row {r:2d}: " + " | ".join(vals))
            
    print("\n--- DATA ROWS (16 to 25) ---")
    for r in range(16, 25):
        vals = [f"{openpyxl.utils.get_column_letter(c)}{r}: '{ws.cell(r, c).value}'" for c in range(1, 16) if ws.cell(r, c).value is not None]
        if vals:
            print(f"Row {r:2d}: " + " | ".join(vals))

