from django.shortcuts import render, get_object_or_404,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from blog import models
from .forms import *
from django.contrib.auth.decorators import login_required

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:profile')
    template_name = 'accounts/signup.html'

    def generate_invoice(self):
        print("hi")
        custom_user, created = models.CustomUser.objects.get_or_create( user=self.object )
        custom_user.save()
        return 1

@login_required
def ProfileView(request):
    post_list =  models.Post.objects.all()
    custom_user, created = models.CustomUser.objects.get_or_create( user=request.user )
    user_posts=[]
    form_post = AddPostForm
    for post in post_list:
        for member in post.member.all():
            if request.user==member.user.user:
                user_posts.append(post)
    context={
        'post_list':user_posts,
        'custom_user':custom_user,
        'form_post':form_post,
    }
    return render(request, 'accounts/profile.html',context=context)


@login_required
def ProfileEdit(request):
    custom_user, created = models.CustomUser.objects.get_or_create( user=request.user )
    form = ProfilePicForm
    context={
        'form':form,
        'custom_user':custom_user,
    }
    return render(request, 'accounts/profile_edit.html',context=context)

def ProfileViewOther(request,username):
    user = get_object_or_404(models.User, username=username)
    post_list =  models.Post.objects.all()
    custom_user, created = models.CustomUser.objects.get_or_create( user=user )
    custom_post_list =  models.CustumPost.objects.all().filter(user=user)
    user_posts=[]
    for post in post_list:
        print(post.member.all())
        for member in post.member.all():
            if user==member.user.user:
                user_posts.append(post)
    context={
        'custom_post_list':custom_post_list,
        'custom_user':custom_user,
        'user_other':user,
        'post_list':user_posts,
    }
    return render(request, 'accounts/profile_other.html',context=context)

def prfilepicchange(request):
    # if this is a POST request we need to process the form data\
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProfilePicForm(request.POST, request.FILES)
        #print(request.FILES['pic'])
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            pic_file = request.FILES['pic']
            custom_user, created = models.CustomUser.objects.get_or_create( user=request.user )
            custom_user.profile_pic = pic_file
            custom_user.save()
            # redirect to a new URL:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProfilePicForm()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def addPost(request):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            # create a form instance and populate it with data from the request:
            # check whether it's valid:
            form_title = form.cleaned_data['title']
            form_text = form.cleaned_data['caption']
            #form_published = form.cleaned_data['published']
            #form_date = form.cleaned_data['pub_date']

            post = models.CustumPost.objects.create(user=request.user,title=form_title,text=form_text)

            post.save()
            custumPost_list= models.CustumPost.objects.all()

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddPostForm()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
