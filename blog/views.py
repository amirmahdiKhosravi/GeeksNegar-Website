from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from .forms import *
from GeeksNegar import settings
from django.views import generic
from django.urls import reverse

def index(request):
    post_list =  models.Post.objects.order_by('-pub_date')
    slider_list= models.Slider.objects.order_by('-id')
    context={'post_list' : post_list, 'slider_list' : slider_list
    }
    return render(request, 'blog/index.html',context=context)

def post_detail(request,post_id='1'):
    post_like_handle(request,post_id)
    obj = get_object_or_404(models.Post, pk=post_id)
    post_like, created = models.Like.objects.get_or_create(post=obj)
    context={'post' : obj,    
            'post_like' : post_like,
            'form_cm' : CommentForm
    }
    return render(request, 'blog/post_detail.html',context=context)

def post_like_handle(request,post_id='1'):
    if request.method == 'POST':
        user = request.user
        create_id = get_object_or_404(models.Post, id=post_id)
        liked, created = models.Like.objects.get_or_create(post=create_id)
        try:
            user_liked = models.Like.objects.get(post=create_id, user=user)
        except:
            user_liked = None

        if user_liked:
            user_liked.likecount -= 1
            liked.user.remove(request.user)
            user_liked.save()
        else:
            liked.user.add(request.user)
            liked.likecount += 1
            liked.save()
        context={'post' : create_id
        }
        return render(request, 'blog/post_detail.html',context=context)


def comment_handler(request,post_id='1'):
    # if this is a POST request we need to process the form data
    obj = get_object_or_404(models.Post, pk=post_id)
    if request.method == 'POST':
        
        print("session 2")
        # create a form instance and populate it with data from the request:
        form = CommentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print("form valid 2")
            # process the data in form.cleaned_data as required
            comment_text = form.cleaned_data['comment_text']
            comment, created = models.Comment.objects.get_or_create( user=request.user , text=comment_text )
            comment.save()
            obj.comments.add(comment)   
            obj.save()         
            # redirect to a new URL:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CommentForm()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
