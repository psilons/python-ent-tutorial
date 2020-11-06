import xlwt

# xlwt works only for xls. For xlsx use openpyxl and XlsxWriter
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('Test2')

bkg = xlwt.Pattern()
bkg.pattern = xlwt.Pattern.SOLID_PATTERN
bkg.pattern_fore_colour = 50

border = xlwt.Borders()
border.left = xlwt.Borders.THIN
border.right = xlwt.Borders.THIN
border.top = xlwt.Borders.THIN
border.bottom = xlwt.Borders.THIN

style = xlwt.XFStyle()
style.pattern = bkg
style.borders = border
style.font = xlwt.Font()
style.font.bold = True
style.font.height = 240
style.alignment = xlwt.Alignment()
style.alignment.horz = xlwt.Alignment.HORZ_CENTER

row = 0
values = [ 'Star Trek', 'Star War' ]
for i, h in enumerate(values):
    sheet.write(row, i, h, style)

row = 1
large_num_style = xlwt.easyxf('', num_format_str='#,##0;[RED]-#,##0;"-"')
sheet.write(row, 0, 1234567890, large_num_style)
sheet.write(row, 1, 1.25, xlwt.easyxf(num_format_str='0.000'))
sheet.write(row, 2, 'abde', xlwt.easyxf('align: horiz right'))
sheet.col(2).width = 2000

workbook.save('d:/tmp/my_test2.xls')
