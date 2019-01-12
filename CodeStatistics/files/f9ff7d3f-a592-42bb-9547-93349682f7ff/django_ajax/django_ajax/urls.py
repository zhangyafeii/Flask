"""django_ajax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path
from app01 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/',views.students),
    path('add_student/',views.add_student),
    path('del_student/',views.del_student),
    path('edit_student/',views.edit_student),
    path('index.html/',views.index),
    path('ajax1.html/',views.ajax1,name='ajax1'),
    path('upload.html/',views.upload),
    re_path('upload_img$',views.upload_img),
    path('jsonp.html',views.jsonp),
    path('ajax3.html',views.ajax3),
]
