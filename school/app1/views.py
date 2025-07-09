from django.shortcuts import render

# Create your views here.

student_data={}

def home(request):
    response=render(request,"app1/index.html")
    return response


def add_student(request):
    name=request.GET.get('name')
    course=request.GET.get('course')
    fee=request.GET.get('fee')
    student_data[name]=[course,fee]
    response=render(request,"app1/index.html",context={"msg":"Student Added"})
    return response


def  add_template(request):
    response=render(request,"app1/add_student.html")
    return response



def display_student(request):
    response=render(request,"app1/display.html",context={"data":student_data})
    return response
