from django.conf.urls import url
from . import views                                  #importing views of this app to joind them to URLS

app_name= 'blog'                                     #to find app's url better and faster

urlpatterns = [
    url(r'^$', views.index , name='index' ), #we used as_view() function to reach Index class of our view
    url(r'^(?P<post_id>[0-9]+)$', views.post_detail , name='post-detail' ),
    url(r'^(?P<post_id>[0-9]+)/add-comment/$', views.comment_handler , name='post-like-handle' ),
    url(r'^aparat/', views.aparat , name='aparat' )
]
