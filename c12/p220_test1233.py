import openpyxl

wb = openpyxl.load_workbook('../resource/excel/example.xlsx')
sheet = wb['Sheet1']

print(sheet['A1'])
print(sheet['A1'].value)

temp = sheet['B1']
print(temp.value)

print('Row %s, Column %s is %s.' % (temp.row, temp.column, temp.value))
print('Cell %s is %s.' % (temp.coordinate, temp.value))

print(sheet['C1'].value)

"""
<Cell 'Sheet1'.A1>
2015-04-05 13:34:02
Apples
Row 1, Column 2 is Apples.
Cell B1 is Apples.
73
"""
