# coding: utf-8
"""Created by chris on 02/07/2017."""
from django import template

register = template.Library()


@register.filter(name="addcssclass")
def addcssclass(field, arg):
    """Add a CSS class to form input"""
    return field.as_widget(attrs={"class": arg})



