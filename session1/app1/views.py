from django.shortcuts import render,redirect

from .models import User



# Create your views here.
def login_view(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        pwd=request.POST.get("password")
    
        try:
            user=User.objects.get(username=uname,password=pwd)
        
        
            #session is created
            request.session['logged_user'] = user.username
            request.session['is_logged'] = True
            
            # here two keys are created.But only one session id is created.
            # 'logged_user' contain 'username' another 'is_logged' contain boolean value

            
            
            
        
            
            return redirect('home')
    
        except User.DoesNotExist:
            return render(request,"app1/login.html",{"error":"Invalid credentials!!!"})  
       
        
    return render(request,"app1/login.html")
    
    
    
def home_view(request):
    if request.session.get("is_logged"):         #here this key 'is_logged' is containing boolean true which only       checks is it logedin or not
        username=request.session.get("logged_user")
        
        session_id=request.session.session_key
        return render(request,"app1/home.html",{"username":username,"session_id":session_id})
    
    return redirect("login")

def logout_view(request):
    request.session.flush()
    return redirect("login")

