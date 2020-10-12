from django import forms

from .models import Post, Tag
from django.forms import ModelForm

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', )
