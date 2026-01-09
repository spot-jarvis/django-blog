from django.contrib import admin

# Register your models here.
from blog.models import Category,Blog
admin.site.register(Category)
admin.site.register(Blog)
