from django.urls import path 
from . import views

app_name = 'blogs'

urlpatterns = [
    path('home/', views.HomePageView.as_view(), name = 'homepage'),
    path('aboutme/', views.AboutMeView.as_view(), name = 'aboutme'),
    path('aboutjob/', views.AboutJobView.as_view(), name = 'aboutjob'),

    path('bloglist/', views.BlogListView.as_view(), name = 'bloglistpage'),
    path('createblog/', views.PostCreateView.as_view(), name = 'createblogpage'),
    
    path('<int:pk>/', views.BlogDetailsView.as_view(), name = 'blogdetailspage'),
    path('<int:pk>/updateblog/', views.PostUpdateView.as_view(), name = 'updateblogpage'),
    path('<int:pk>/deleteblog/', views.PostDeleteView.as_view(), name = 'deleteblogpage'),

    


    
    
]
    
    