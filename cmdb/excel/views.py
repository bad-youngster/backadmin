# -*- coding: utf-8 -*-
import xlwt
from django.http import HttpResponse

from cmdb import models


def export_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment;filename="test.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('test')
    row_num = 0
    font_style = xlwt.XFStyle()
    columns = ['name', 'code', 'memo']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = models.Status.objects.all().values_list('name', 'code', 'memo')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response
