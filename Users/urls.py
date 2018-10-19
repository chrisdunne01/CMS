from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView
from Users.models import Post


urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Post.objects.all(), template_name="Users/Users.html")),
    url(r'^signup/$', views.signup, name='signup')
    # url(r'^$', views.index, name='index')
]
