import openpyxl

wb = openpyxl.load_workbook('live_monitoring.xlsx', data_only=False)

for name in wb.sheetnames:
    ws = wb[name]
    print(f"\n==================== FORMULAS & CELLS: {name} ====================")
    for r in range(1, ws.max_row + 1):
        row_cells = []
        for c in range(1, ws.max_column + 1):
            val = ws.cell(r, c).value
            if val is not None:
                row_cells.append(f"C{c}({openpyxl.utils.get_column_letter(c)}{r})='{val}'")
        if row_cells:
            print(f"Row {r:2d}: " + " ; ".join(row_cells))

