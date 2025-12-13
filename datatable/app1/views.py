from django.shortcuts import render
from app1.models import Car
from django.http import JsonResponse

# Create your views here.

def carlist(request):
    return render(request,"app1/carlist.html")

def carapi(request): #It is providing the data through the url -> template
    cars=Car.objects.all()
    
    data=[]
    for c in cars:
        data.append({
            "id":c.id,
            "name":c.name,
            "colour":c.colour,
            
        })
        
    return JsonResponse({"data":data})