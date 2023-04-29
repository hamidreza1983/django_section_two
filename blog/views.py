from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, RedirectView , ListView, DetailView, FormView
from .models import Post
from .forms import PostCreateForm

    
class RedirectToBlog(RedirectView):
    url = '/blog/'
    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)
    
class PostListView(ListView):
    queryset = Post.objects.filter(status=True)
    context_object_name = 'posts'
    paginate_by = 4
    ordering = 'id'  
    
    
class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'


class PostCreateView(FormView):
    template_name = "home/create_post.html"
    form_class = PostCreateForm
    success_url = "/blog/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

