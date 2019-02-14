# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect

from cmdb import models


def cmdb(request):
    if request.method == "GET":
        return render(request,'devicelist.html')
    if request.method == "POST":
        name = request.POST.get("name", None)
        code = request.POST.get("code", None)
        memo = request.POST.get("memo", None)
        statusadd = models.Status.objects.create(name=name, code=code, memo=memo)
        statusadd.save()

    return redirect(request, "devicelist.html")


def new(request):
    return render(request, "new.html")


def insert(request):
    return render(request, 'devicestatus.html')


def list(request):

    status_list = models.Status.objects.all()
    return render(request, 'cmdbindex.html', {"status_list": status_list})
