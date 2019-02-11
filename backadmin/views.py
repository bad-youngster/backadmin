from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def table(request):
    return render(request,"tables.html")

def test(request):
    return render(request,"test.html")
