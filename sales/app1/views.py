from django.shortcuts import render

# Create your views here.
def index(request):
    response = render(request,'app1/index.html')
    return response


def display(request):
    sales_data={2010:45000,2011:56000,2012:67000,2013:78000,2014:89000,2015:100000}
    response=render(request,"app1/display.html",context={'sales_data':sales_data})
    return response