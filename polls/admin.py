from django.contrib import admin
from .models import Category, Comment, Article


admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Comment)
