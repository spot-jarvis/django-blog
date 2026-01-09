from django.contrib import admin

# Register your models here.
from blog.models import Category,Blog

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    search_fields = ('id', 'title', 'status','category')
    list_editable = ('is_featured', )

class CategoryAdmin(admin.ModelAdmin):
    list_display =('catogory_name', 'created_at', 'updated_at')
    search_fields = ('id', 'catogory_name')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Blog,BlogAdmin)