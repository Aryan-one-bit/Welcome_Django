from django.shortcuts import render

# Create your views here.
def signin(request):
    users={'Naresh':'n123',
           'Suresh':'s123',
           'Ramesh':'r123'}
    
    uname=request.GET['uname']
    pwd=request.GET['pwd']

    if uname in users and users[uname]==pwd:
        response=render(request,"app1/welcome.html",context={'uname':uname})
        return response
    
    else:
        response=render(request,"app1/login.html",context={'msg':'Invalid password or username'})
        return response
    

def login(request):
    response=render(request,"app1/login.html")
    return response