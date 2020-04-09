import openpyxl

# 将这个数字改为 input 应付 25 个字母的乘法表
num = 10

wb = openpyxl.Workbook()
sheet = wb.active

az = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(1, num + 1):
    sheet['A' + str(i + 1)] = i
    sheet[az[i] + '1'] = i

for i in range(2, num + 2):
    for j in range(2, num + 2):
        index = az[i - 1] + str(j)
        sheet[index] = (i - 1) * (j - 1)


wb.save('../resource/excel/multiplicationTable.xlsx')
print('Done')
