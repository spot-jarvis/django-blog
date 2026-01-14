from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import Category, Blog
def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured = True, status = 'Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured = False,status = 'Published')
    return render(request,'blog/home.html',{
        'contexts' : categories,
        'is_featured' : featured_posts,
        'posts' : posts
    })

def posts_by_category(request,category_id):
    posts = Blog.objects.filter(category_id = category_id, status = 'Published').order_by('updated_at')
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    return render(request, "blog/tech.html",{
        "posts" : posts,
        'category' : category
    })