import openpyxl

wb = openpyxl.load_workbook(r'C:\Users\HP\Projects\APlikasi MBG\drive_template.xlsx', data_only=True)
print('Sheet names:', wb.sheetnames)

for name in wb.sheetnames:
    ws = wb[name]
    print(f'\n================ Sheet: {name} (Rows: {ws.max_row}, Cols: {ws.max_column}) ================')
    for r in range(1, min(25, ws.max_row + 1)):
        vals = [str(ws.cell(r, c).value) if ws.cell(r, c).value is not None else '' for c in range(1, min(20, ws.max_column + 1))]
        if any(v.strip() for v in vals):
            # Print non-empty
            row_str = ' | '.join(vals[:12])
            print(f'R{r:02d}: {row_str}')

print("\n--- FORMULAS AND FULL COLUMNS (Sheet 1) ---")
wb_raw = openpyxl.load_workbook(r'C:\Users\HP\Projects\APlikasi MBG\drive_template.xlsx', data_only=False)
ws_raw = wb_raw['Monitoring Alur Bahan Baku']
for r in range(15, 30):
    row_vals = [f"C{c}:{ws_raw.cell(r, c).value}" for c in range(1, 16) if ws_raw.cell(r, c).value is not None]
    if row_vals:
        print(f"Row {r:02d}:", " | ".join(row_vals))
