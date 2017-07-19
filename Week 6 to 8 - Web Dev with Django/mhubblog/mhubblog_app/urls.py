# coding: utf-8
"""Define url routes for mhubblog application"""
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', view=views.index, name="index"),  # Homepage

    url(r'^articles/$', view=views.articles, name="articles-list"),
    url(r'^article/create/$', view=views.create_article, name="create-article"),
    url(r'^articles/(?P<slug>[-\w]+)/$', view=views.article_detail, name="article-detail"),
    url(r'^articles/(?P<slug>[-\w]+)/update/$', view=views.update_article, name="update-article"),
    url(r'^articles/(?P<slug>[-\w]+)/delete/$', view=views.delete_article, name="delete-article"),
]
