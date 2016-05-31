from django.contrib import admin

# Register your models here.
from blog.models import Article, Category, Tag

admin.site.register([Article, Category, Tag])
