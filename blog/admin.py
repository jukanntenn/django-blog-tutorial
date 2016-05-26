from django.contrib import admin

# Register your models here.
from blog.models import Article, Category

admin.site.register(Article)
admin.site.register(Category)