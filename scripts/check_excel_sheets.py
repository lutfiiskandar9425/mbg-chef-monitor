import openpyxl

wb = openpyxl.load_workbook('live_monitoring.xlsx', data_only=True)
for sheet in wb.sheetnames:
    print('='*50)
    print('SHEET:', sheet)
    ws = wb[sheet]
    for r in range(1, 25):
        row_vals = [str(ws.cell(r, c).value or '') for c in range(1, 8)]
        if any(row_vals):
            print(f'R{r}:', ' | '.join(row_vals[:6]))

