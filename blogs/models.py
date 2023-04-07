from django.db import models
from django.shortcuts import reverse
class BlogList(models.Model):

    STATUS_CHOICES = (
        ('pub', 'published'),
        ('drf', 'draft'),
    )

    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status= models.CharField(choices= STATUS_CHOICES, max_length=3)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blogs:blogdetailspage", args=[self.pk])
    
    # def get_absolute_url(self):
    #     return reverse("blogs:blogdetailspage", kwargs={"pk": self.pk})
    
    