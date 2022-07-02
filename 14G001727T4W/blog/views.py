from django.shortcuts import render
from .models import Post
from django.views.generic import CreateView
# Create your views here.
class PostCreateView(CreateView):
    model=Post
    fields="__all__"
    template_name="index.html"