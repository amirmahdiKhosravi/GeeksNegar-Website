from django.conf.urls import url

from . import views

app_name= 'accounts'
urlpatterns = [
    url(r'^signup/$', views.SignUp.as_view(), name='signup'),
    url(r'^profile/$', views.ProfileView, name='profile'),
    url(r'^profile/(?P<username>[a-zA-Z0-9]+)$', views.ProfileViewOther, name='profile-other'),
    url(r'^profile/post/create/$', views.ProfilePostCreat, name='PostCreat'),
    url(r'^profile/post/(?p<pk>\d+)/update/$', views.ProfilePostUpdate, name='PostUpdate'),
    url(r'^profile/post/(?p<pk>\d+)/delete/$', views.ProfilePostDelete, name='PostDelete ')
]
