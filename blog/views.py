from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Category
def home(request):
    categories = Category.objects.all()
    return render(request,'blog/home.html',{
        'contexts' : categories
    })