"""
http://pythonexcels.com/python-excel-mini-cookbook/
"""
import win32com.client as win32
import os
excel = win32.DispatchEx('Excel.Application')
excel.Visible = True  # use False if you don't want to see it
excel.DisplayAlerts = False  # turn off popup boxes

excel_file = os.getcwd() + '/my_test.xlsx'  # relative path not working?
workbook = None
sheet = None
if os.path.isfile(excel_file):
    workbook = excel.Workbooks.Open(excel_file)
    # sheet = workbook.Worksheets[0]
    sheet = excel.ActiveSheet
    sheet.Name = 'Test'
else:
    workbook = excel.Workbooks.Add()
    sheet = workbook.Worksheets.Add()
    sheet.Name = 'Test'
    workbook.SaveAs(excel_file)

row = 1
col = 1
sheet.Cells(row, col).Value = "Test1"
sheet.Cells(row, col).Interior.ColorIndex = 23
sheet.Cells(row, col).Font.ColorIndex = 2
sheet.Cells(row, col).Font.Bold = True

# we may macro with active sheet: excel.Run('macro name')

workbook.Save()
workbook.Close(SaveChanges=True)

excel.Quit()
del sheet
del workbook
del excel
