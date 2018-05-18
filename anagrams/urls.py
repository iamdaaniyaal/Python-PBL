"""anagrams URL Configuration

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')
"""
from django.contrib import admin
from django.urls import path, include
# from anagramsapp.views import index as myindex

# from anagramsapp.views import first as myfirst
from anagramsapp import views

urlpatterns = [
	path('',views.index,name='index'),
	path('e1/',views.easy_first,name='easy_first'),
    path('e2/',views.easy_second,name='easy_second'),
    path('e3/',views.easy_third,name='easy_third'),
    path('e4/',views.easy_fourth,name='easy_fourth'),
    path('e5/',views.easy_fifth,name='easy_fifth'),
    path('m1/',views.med_first,name='med_first'),
    path('m2/',views.med_second,name='med_second'),
    path('m3/',views.med_third,name='med_third'),
    path('m4/',views.med_fourth,name='med_fourth'),
    path('m5/',views.med_fifth,name='med_fifth'),
    path('finish',views.finish,name='finish'),
    path('admin/', admin.site.urls),

]
