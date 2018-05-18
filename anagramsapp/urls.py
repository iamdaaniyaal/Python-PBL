from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
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
]
