<<<<<<< HEAD
from django.shortcuts import render
||||||| merged common ancestors
from django.shortcuts import render, get_object_or_404
=======
from django.shortcuts import render, get_object_or_404,HttpResponseRedirect
>>>>>>> 9168e2e508f92329a18acb9eb806cd60d6f95f9d
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from blog import models
from .forms import *

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:profile')
    template_name = 'accounts/signup.html'

def ProfileView(request):
    post_list =  models.Post.objects.all()
    user_posts=[]
    form = ProfilePicForm
    for post in post_list:
        print(post.member.all())
        for member in post.member.all():
            if request.user==member.user:
                print(post)
                user_posts.append(post)
    context={
        'form':form,
        'post_list':user_posts,
    }
    return render(request, 'accounts/profile.html',context=context)

<<<<<<< HEAD
class ProfilePostCreatee(generic.CreateView):
    model=models.Post
    fields= '__all__'


class ProfilePostDelete(generic.DeleteView):
    model=models.Post
    fields= '__all__'

class ProfilePostUpdate(generic.UpdateView):
    model=models.Post
    fields= '__all__'
    success_url = reverse_lazy('accounts:profile')
||||||| merged common ancestors
def ProfileViewOther(request,username):
    user = get_object_or_404(models.User, username=username)
    post_list =  models.Post.objects.all()
    user_posts=[]
    for post in post_list:
        print(post.member.all())
        for member in post.member.all():
            if user==member.user:
                print(post)
                user_posts.append(post)
    context={
        'user_other':user,
        'post_list':user_posts,
    }
    return render(request, 'accounts/profile_other.html',context=context)
=======
def ProfileViewOther(request,username):
    user = get_object_or_404(models.User, username=username)
    post_list =  models.Post.objects.all()
    user_posts=[]
    for post in post_list:
        print(post.member.all())
        for member in post.member.all():
            if user==member.user:
                print(post)
                user_posts.append(post)
    context={
        'user_other':user,
        'post_list':user_posts,
    }
    return render(request, 'accounts/profile_other.html',context=context)

def prfilepicchange(request,username):
    # if this is a POST request we need to process the form data\
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProfilePicForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            pic_file = request.POST.get('pic')
            custom_user, created = models.CustomUser.objects.get_or_create( user=request.user , profile_pic=pic_file )
            custom_user.save()
            # redirect to a new URL:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

<<<<<<< HEAD
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
>>>>>>> 6e19180425e193469640ce8c086e4f171a8cf3ce
||||||| merged common ancestors
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
=======
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProfilePicForm()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
>>>>>>> 9168e2e508f92329a18acb9eb806cd60d6f95f9d
