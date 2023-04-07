from django import forms
from .models import BlogList

class CreateBlogForm(forms.ModelForm):
    class Meta:
            model = BlogList
            fields = ['title', 'text', 'author', 'status']