import win32com.client as win32
import os

cwd = os.getcwd()
excel = win32.DispatchEx("Excel.Application")
excel.Visible = True
workbook = excel.Workbooks.Open(cwd + '/test_xls.xlsx')
worksheet1 = workbook.Worksheets[0]

worksheet1.Name = "My sheet1"  # change its name

worksheet1.Cells(1, 1).Value = "Hello, Excel"  # change the cell value
print(worksheet1.Cells(1, 1).Value)

for i in range(1, 5):
    worksheet1.Cells(2, i).Value = i
    
worksheet1.Range(worksheet1.Cells(3, 1), worksheet1.Cells(3, 4)).Value = [5, 6, 7, 8]
worksheet1.Range('A4:D4').Value = [i for i in range(9, 13)]
worksheet1.Cells(5, 4).Formula = '=SUM(A2:A4)'

worksheet1.Cells(5, 4).Font.Size = 16
worksheet1.Cells(5, 4).Font.Bold = True
# FileFormat=6, csv format, chech others
print(cwd[0:2] + '/myexcel.xlsx')
workbook.SaveAs(cwd + '/myexcel.xlsx')  # won't return until yes/no dialog is clicked if file exists already
workbook.Close(SaveChanges=0)

excel.Quit()
