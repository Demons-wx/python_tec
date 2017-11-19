# coding=utf-8

# 小学某班成绩，记录在excel文件中：
'''
姓名  语文  数学  外语
李雷  95    99    96
韩梅  98    100   93
张峰  94     95   95
'''
# 利用python读写excel，添加总分列，计算每人总分
#
#
# 使用pip安装 pip install xlrd xlwt
# 使用第三方库xlrd和xlwt，这两个库分别用于excel读和写

import xlrd, xlwt

rbook = xlrd.open_workbook('grade.xlsx')
rsheet = rbook.sheet_by_index(0)

nc = rsheet.ncols
rsheet.put_cell(0, nc, xlrd.XL_CELL_TEXT, u'总分', None)

for row in xrange(1, rsheet.nrows):
    t = sum(rsheet.row_values(row, 1))
    rsheet.put_cell(row, nc, xlrd.XL_CELL_NUMBER, t, None)

wbook = xlwt.Workbook()
wsheet = wbook.add_sheet(rsheet.name)
style = xlwt.easyxf('align: vertical center, horizontal center')

for r in xrange(rsheet.nrows):
    for c in xrange(rsheet.ncols):
        wsheet.write(r, c, rsheet.cell_value(r, c), style)

wbook.save('output.xlsx')