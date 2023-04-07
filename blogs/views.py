from django.urls import reverse_lazy
from django.views import generic 

from .models import BlogList
from .forms import CreateBlogForm

from django.shortcuts import render , redirect, reverse , get_object_or_404 
from django.contrib.auth.models import User


class HomePageView(generic.TemplateView):
    template_name = 'blogs/home.html'
    
class BlogListView(generic.ListView):
    template_name = 'blogs/bloglist.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
            return BlogList.objects.filter(status = 'pub').order_by('datetime_modified')

class BlogDetailsView(generic.DetailView):
    model = BlogList
    template_name = 'blogs/blogdetails.html'
    context_object_name = 'blog_post'
    
class PostCreateView(generic.CreateView):
    form_class = CreateBlogForm
    template_name = 'blogs/createblog.html'
    context_object_name = 'form'
    
class PostUpdateView(generic.UpdateView):
    model = BlogList
    form_class = CreateBlogForm
    template_name = 'blogs/createblog.html'
    context_object_name = 'form'

class PostDeleteView(generic.DeleteView):
    model = BlogList
    template_name = 'blogs/deleteblog.html'
    context_object_name = 'post'
    success_url = reverse_lazy('blogs:bloglistpage')

class AboutMeView(generic.TemplateView):
    template_name = 'blogs/aboutme.html'

class AboutJobView(generic.TemplateView):
    template_name = 'blogs/aboutjob.html'
