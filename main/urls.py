from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('experience/', views.experience, name='experience'),
    path('technologies/', views.technologies, name='technologies'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog_list, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    # Add this to urlpatterns
    path('projects/', views.projects, name='projects'),
    path('books/', views.books, name='books'),
]