from django.shortcuts import render,redirect

# Create your views here.
def set_session_view(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        city=request.POST.get('city')
        
        #session creation
        
        request.session['session_name']=name
        request.session['session_city']=city
        request.session['is_active']=True
        
        return redirect('get_session')
    
    return render(request,"app1/set_session.html")
    
def get_session_view(request):
    if request.session.get('is_active'):
        
        
        data={
            "name":request.session.get("session_name"),
            "city":request.session.get("session_city"),
            "session_id":request.session.session_key,
            "all_data":dict(request.session.items()),
        }
        return render(request,"app1/get_session.html",data)
    
    
    message="No active session found..."
    return render(request,"app1/set_session.html",{"message":message})
    
    
def delete_session_view(request):
    request.session.flush()
    message2="Session deleted successfully..."
    return render(request,"app1/set_session.html",{'message2':message2})