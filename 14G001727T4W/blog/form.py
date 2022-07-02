from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Post
from django import  forms




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"