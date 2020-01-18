from django.conf.urls import url

from . import views

app_name= 'accounts' 
urlpatterns = [
    url(r'^signup/$', views.SignUp.as_view(), name='signup'),
    url(r'^profile/$', views.ProfileView, name='profile'),
]