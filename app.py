import openpyxl as op 

wb = op.load_workbook('transactions.xlsx')
sheet = wb['Sheet1']

for row in range(2,sheet.max_row+1):
    original_value = sheet.cell(row,3).value
    correct_value = original_value * 0.9
    sheet.cell(row,4).value = correct_value

wb.save('transactions2.xlsx')