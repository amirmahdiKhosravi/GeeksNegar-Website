from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from GeeksNegar import settings

def index(request):
    post_list =  models.Post.objects.order_by('-pub_date')
    context={'post_list' : post_list
    }
    return render(request, 'blog/index.html',context=context)
