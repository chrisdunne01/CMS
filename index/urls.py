from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    # path('/', views.index, name='index'),
    # path('/', views.index, name='index')
    url(r'^$', views.index, name='index')

    # url(r'/Users^$', views.index, name='index')

]


