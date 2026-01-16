from django.shortcuts import render,redirect,get_object_or_404
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
    category = get_object_or_404(Category, pk = category_id)
    return render(request, "blog/tech.html",{
        "posts" : posts,
        'category' : category
    })  