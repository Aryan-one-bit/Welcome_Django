"""
URL configuration for dbdemo3student project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from stud.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('add_temp/', add_student_template, name='add_temp'),
    path('add/',add_student, name='add_student'),
    path('update_temp/', update_student_template, name='update_temp'),
    path('update/', update_student, name='update_student'),
    path('delete_temp/', delete_student_template, name='delete_temp'),
    path('delete/', delete_student, name='delete_student'),
    path('find_temp/', find_result_template, name='find_temp'),
    path('find/',find_result, name='find_student'),
    path('view/',view_student, name='view_student'),
    

]
