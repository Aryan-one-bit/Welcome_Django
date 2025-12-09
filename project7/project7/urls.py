"""
URL configuration for project7 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from std.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', step_container, name='step_container'),
    path('load-step/<int:step>/', load_step, name='load_step'),
    path('save-step/<int:step>/', save_step, name='save_step'),
    path('submit-final/', submit_final, name='submit_final'),

]
