# coding: utf-8
"""Build HTML create and update forms for DB model"""
from django import forms
from .models import Category, Article


class ArticleForm(forms.ModelForm):
    """HTML create and update form for Article DB model"""
    class Meta:
        model = Article
        fields = ["title", "image", "content", "categories"]
        category = forms.ModelMultipleChoiceField(
                queryset=Category.objects.all(),
                to_field_name="categories"
        )
