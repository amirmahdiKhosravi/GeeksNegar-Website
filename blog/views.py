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

def post_detail(request,post_id='1'):
    obj = get_object_or_404(models.Post, pk=post_id)
    context={'post' : obj
    }
    return render(request, 'blog/post_detail.html',context=context)




# def index(request):
#     post_list =  models.Post.objects.order_by('-pub_date')
#     context={'post_list' : post_list
#     }
#     return render(request, 'blog/index.html',context=context)
