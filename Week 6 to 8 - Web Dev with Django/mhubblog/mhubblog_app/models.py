# coding: utf-8
"""DB models  for mhubblog application"""
from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Category(models.Model):
    """Categories to be defined for a given Article"""
    title = models.CharField(max_length=30, help_text=_("Enter an article category name"))
    color = models.CharField(max_length=10, help_text=_("Enter a class name representing the category color"))

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        """Returns a human-readable string representation of an Article for Python 2"""
        return self.title

    def __str__(self):
        """Returns a human-readable string representation of an Article for Python 3"""
        return self.title


@python_2_unicode_compatible
class Article(models.Model):
    """Defines the properties of an Article"""
    publisher = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=700)
    slug = models.SlugField(unique=True)
    image = models.FileField(blank=True, null=True, upload_to="uploads/")
    content = models.TextField()
    categories = models.ManyToManyField("Category", related_name="articles")
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def display_categories(self):
        """Display a comma-separated string of associated categories"""
        return ", ".join([category.title for category in self.categories.all()])
    display_categories.short_description = "Categories"

    def get_absolute_url(self):
        """Returns the absolute url to the detail view of an article"""
        return reverse("mhubblog_app:article-detail", kwargs={"slug": self.slug})
    
    def __unicode__(self):
        """Returns a human-readable string representation of an Article for Python 2"""
        return self.title

    def __str__(self):
        """Returns a human-readable string representation of an Article for Python 3"""
        return self.title


def create_slug(instance, new_slug=None):
    """Create a unique slug for an article"""
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Article.objects.filter(slug=slug).order_by("-id")
    slug_exists = qs.exists()
    if slug_exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


# Create a receive function for a pre_save signal on Article
def pre_save_receiver(sender, instance, *args, **kwargs):
    """Article pre_save receiver"""
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(receiver=pre_save_receiver, sender=Article)



