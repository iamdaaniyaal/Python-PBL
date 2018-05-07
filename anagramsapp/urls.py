from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('1/<slug:id>/',views.first,name='first'),
    path('1/<slug:id>/',views.first1,name='first1'),
    path('done/',views.done,name='done'),
    # path('1/',views.first,name='first'),
    # path('2/',views.second,name='second'),
]
