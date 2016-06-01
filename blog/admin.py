from django.contrib import admin

# Register your models here.
from blog.models import Article, Category, Tag


# Add in this class to customized the Admin Interface
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


# Update the registeration to include this customised interface
admin.site.register(Article, ArticleAdmin)

admin.site.register([Category, Tag])
