from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('',PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='blog-single'),
    path('post-create/',PostCreateView.as_view(), name='post-create'),
    path('post-update/<int:pk>/',PostUpdateView.as_view(), name='post-update'),
    path('post-delete/<int:pk>/',PostDeleteView.as_view(), name='post-delete'),
    ]
