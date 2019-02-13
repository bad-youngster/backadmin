# -*- coding: utf-8 -*-
from django.shortcuts import render

from cmdb import models


def cmdb(request):
    return render(request, "cmdbindex.html")

def new(request):
    return render(request,"new.html")

def insert(request):
    if request.method == "POST":
        name = request.POST.get("name",None)
        code = request.POST.get("code",None)
        memo = request.POST.get("memo",None)
        statusadd = models.Status.objects.create(name=name,code=code,memo=memo)
        statusadd.save()
    return render(request,'devicestatus.html')

def list(request):
    status_list = models.Status.objects.all()
    return render(request,'devicelist.html',{"status_list": status_list})

