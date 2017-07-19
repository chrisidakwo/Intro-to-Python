# coding: utf-8
from django.contrib import admin
from .models import Category, Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Customize the Article admin view"""
    list_display = ("title", "publisher", "display_categories", "date_created", "last_updated")
    list_filter = ["categories", "last_updated", "date_created"]
    fieldsets = (
        ("", {
           "fields": ("publisher", "title", "image", "content", "categories")
        }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Customize the Category admin view"""
    list_display = ("title", "color")
