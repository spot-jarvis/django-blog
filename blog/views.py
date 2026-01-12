from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Category, Blog
def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured = True, status = 'Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured = False,status = 'Published')
    print(posts)
    return render(request,'blog/home.html',{
        'contexts' : categories,
        'is_featured' : featured_posts,
        'posts' : posts
    })