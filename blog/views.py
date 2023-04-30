from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import (
    TemplateView, RedirectView , ListView, DetailView, FormView, CreateView, UpdateView,DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Post
from .forms import PostCreateForm

    
class RedirectToBlog(RedirectView):
    url = '/blog/'
    
    
class PostListView(PermissionRequiredMixin,ListView):
    permission_required = ["blog.view_post"]
    queryset = Post.objects.filter(status=True)
    context_object_name = 'posts'
    paginate_by = 4
    ordering = 'id'  
    
    
class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'


#class PostCreateView(FormView):
#    template_name = "home/create_post.html"
#    form_class = PostCreateForm
#    success_url = "/blog/"#

#    def form_valid(self, form):
#        form.save()
#        return super().form_valid(form)#

class PostCreateView(CreateView):
    model = Post
    #fields = ['author','title','content','status','category','published_date']
    form_class = PostCreateForm
    template_name = "home/create_post.html"
    success_url = "/blog/"
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.status = False
        form.instance.published_date =None
        return super().form_valid(form)
    
class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = "blog/update_post.html"
    success_url = "/blog/"


class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = "/blog/"
