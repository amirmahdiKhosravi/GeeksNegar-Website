from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from GeeksNegar import settings
from django.views import generic

class Index(generic.TemplateView):
    
    template_name='blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = models.Post.objects.order_by('-pub_date')
        return context




# def index(request):
#     post_list =  models.Post.objects.order_by('-pub_date')
#     context={'post_list' : post_list
#     }
#     return render(request, 'blog/index.html',context=context)
