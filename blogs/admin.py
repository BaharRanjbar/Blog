from django.contrib import admin

from .models import BlogList

@admin.register(BlogList)

class PostListAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status')
    ordering = ('datetime_created',)
