from django.shortcuts import render
from Reg.models import User
from django.db.models import Q
# Create your views here.

def home(request):
    response = render(request, 'Reg/index.html')
    return response

def signup_temp(request):
    return render(request,"Reg/signup_temp.html")

def signup(request):
    name=request.GET.get('name')
    uname=request.GET.get('uname')
    pwd=request.GET.get('pwd')
    qs=User.objects.filter(Uname=uname)

    if len(qs) == 0:
        u=User(Name=name,Uname=uname,Password=pwd)
        u.save()
        msg="User Registered successfully"
    else:
        msg="User already exists"

    return render(request,"Reg/signup_temp.html",context={"msg":msg})


def signin_temp(request):
    return render(request,"Reg/signin_temp.html")

def signin(request):
    uname=request.GET.get('uname')
    pwd=request.GET.get('pwd')
    qs=User.objects.filter(Q(Uname=uname) & Q(Password=pwd))

    if len(qs)==0:
        msg="Invalid Username or password"
        return render(request,"Reg/signin_temp.html",context={"msg":msg})
    else:
        msg="Login Successful"
        return render(request,"Reg/welcome_temp.html",context={"msg":msg,'uname':uname})
    


def resetpwd_temp(request):
    return render(request,"Reg/resetpwd_temp.html")

def resetpwd(request):
    uname=request.GET.get('uname')
    opwd=request.GET.get('opwd')
    npwd=request.GET.get('npwd')
    u=User.objects.filter(Q(Uname=uname) & Q(Password=opwd)).update(Password=npwd)
    if u==0:
        msg="Invalid Username or password"
        return render(request,"Reg/resetpwd_temp.html",context={"msg":msg})
    else:
        msg="Password updated successfully"
        return render(request,"Reg/resetpwd_temp.html",context={"msg":msg})
