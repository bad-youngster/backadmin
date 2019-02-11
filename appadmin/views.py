from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import render, redirect

from appadmin import models
from appadmin.forms import RegisterForm, LoginForm

from appadmin.models import registra
from appadmin.verification import check_code


def register(request):
    registraform = RegisterForm(request.POST)
    # if request.method == 'GET':
    #     return render(request, 'index.html')

    if registraform.is_valid():
            firstname = request.POST.get('firstname', None)
            lastname = request.POST.get('lastname', None)
            email = request.POST.get('email', None)
            password = request.POST.get('password', None)
            verfiypassword = request.POST.get('verfiypassword', None)

            registeradd = registra.objects.create(firstname=firstname,
                                                  lastname=lastname,
                                                  email=email,
                                                  password=password,
                                                  verfiypassword=verfiypassword,
                                                  )
            print(registeradd)
            registeradd.save()

    return render(request, "register.html")

def getcheck_code(request):
    code = check_code.getCheckChar()
    img = check_code.getImg(code)
    f = BytesIO()
    img.save(f,'PNG')
    request.session['check_code'] = code
    return HttpResponse(f.getvalue())

def login_page(request):
    if request.method == "GET":
        return render(request,'login.html')
    if request.method == 'POST':
        obj = LoginForm(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
            check_dic = models.LoginModels.objects.filter(**obj.cleaned_data).first()
            if check_dic is None:
                return render(request,'login.html')
            else:
                checkcode = request.POST.get('checkcode')
                if checkcode.upper() == request.session['check_code'].upper():
                    request.session['userid'] = obj.cleaned_data['username']
                    request.session['is_login'] = True
                    return render(request,'welcome.html')
                else:
                    return render(request,'login.html',{'err_checkcode':"code error"})
        else:
            return render(request,'login.html',{'obj':obj})


def welcome(request):
    if request.session.get('is_login',None):
        return render(request,'welcome.html')
    else:
        return redirect('/login/')

