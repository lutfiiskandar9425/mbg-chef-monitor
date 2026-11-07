import openpyxl

wb = openpyxl.load_workbook('live_monitoring.xlsx', data_only=True)
for name in wb.sheetnames:
    ws = wb[name]
    print(f"\n==================== SHEET: {name} (Rows: {ws.max_row}, Cols: {ws.max_column}) ====================")
    for r in range(1, min(ws.max_row + 1, 35)):
        row_vals = [ws.cell(r, c).value for c in range(1, min(ws.max_column + 1, 18))]
        # Only print non-empty rows
        if any(v is not None for v in row_vals):
            formatted = [str(v) if v is not None else "" for v in row_vals]
            print(f"Row {r:2d}: {' | '.join(formatted[:15])}")

