# -*- coding: utf-8 -*-
from venv import logger

import xlrd
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render

from cmdb import models


def excel_upload(request):
    if request.method == 'POST':
        f = request.FILES.get('excel_file')  # 读取excel文件
        type_excel = f.name.split('.')[1]
        if type_excel in ['xlsx', 'xls']:
            wb = xlrd.open_workbook(filename=None, file_contents=f.read(), formatting_info=True)  # 解析上传的excel
            table = wb.sheets()[0]  # 导入第一个sheets
            rows = table.nrows  # 行数
            try:
                with transaction.atomic():
                    for i in range(1, rows):
                        rowVlaues = table.row_values(i)
                        major = models.Status.objects.filter(majorid=rowVlaues[1]).first()
                        models.Status.objects.bulk_create(gradeid=rowVlaues[0], major=major, gradename=rowVlaues[2],
                                                          memo=rowVlaues[3])
            except:
                # logger.error('解析excel文件或者数据插入错误')
                return render(request, 'success.html', {'message': '导入成功'})
        else:
            # logger.error('上传文件类型错误')
            return render(request, 'failed.html', {'message': '导入失败'})
