from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'^$', ListView.as_view(queryset=Post.objects.all(), template_name="Users/Users.html"))
    # url(r'^signup$', views.signup, name='signup'),
    url(r'^$', views.index),
    url(r'^register/$', views.register, name='register')

    # url(r'^Profile$', views.index, name='index')
]
