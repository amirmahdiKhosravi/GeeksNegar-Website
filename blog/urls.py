from django.conf.urls import url
from . import views                                  #importing views of this app to joind them to URLS

app_name= 'blog'                                     #to find app's url better and faster

urlpatterns = [
    url(r'^$', views.Index.as_view(),name='index' ) #we used as_view() function to reach Index class of our view
]
