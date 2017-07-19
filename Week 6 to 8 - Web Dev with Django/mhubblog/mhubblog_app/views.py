# coding: utf-8
"""View controller for mhub blog application"""
from django.contrib import messages
from django.core.paginator import (Paginator, PageNotAnInteger, EmptyPage)
from django.http import Http404
from django.utils.lorem_ipsum import COMMON_P
from django.shortcuts import (render, get_object_or_404, redirect)
from .models import Article
from .forms import ArticleForm
from django.contrib.auth import logout as lgout
from django.contrib.auth.decorators import login_required

# C - Create        --- POST/PUT
# R - Retrieve/Read --- GET
# U - Update        --- POST/PUT
# D - Delete        --- POST


def index(request):
    """Homepage for all posts"""
    article_list = Article.objects.all().order_by("-date_created")[:10]
    context = {
        "articles": article_list
    }
    return render(request, "mhubblog_app/index.html", context)


def articles(request):
    """View controller for articles_list page"""
    article_list = Article.objects.all().order_by("-date_created")
    paginator = Paginator(article_list, 5)
    page = request.GET.get("page")

    try:
        article_list = paginator.page(page)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    except EmptyPage:
        article_list = paginator.page(paginator.num_pages)

    context = {
        "articles": article_list,
    }
    return render(request, "mhubblog_app/articles_list.html", context)


def article_detail(request, slug):
    """View controller for an individual article"""
    article = get_object_or_404(Article, slug=slug)
    context = {
        "article": article,
    }
    return render(request, "mhubblog_app/article_detail.html", context)


@login_required
def create_article(request):
    """Create a new article"""
    if request.method != "POST":
        form = ArticleForm()  # Render the form
    else:
        form = ArticleForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.content = COMMON_P
            article.save()
            form.save_m2m()
            messages.success(request, "Post successfully created!")
        return redirect(to="mhubblog_app:index")

    context = {
        "form": form,
    }
    return render(request, "mhubblog_app/article_create.html", context)


def update_article(request, slug):
    """Update an article content"""
    article = get_object_or_404(Article, slug=slug)
    if request.method != "POST":
        form = ArticleForm(instance=article)
    else:
        form = ArticleForm(data=request.POST, instance=article)
        if form.is_valid():
            form.save()
        return redirect(to="mhubblog_app:index")

    context = {
        "article": article,
        "form": form,
    }
    return render(request, "mhubblog_app/article_update.html", context)


def delete_article(request, slug):
    """Delete an existing article"""
    article = get_object_or_404(Article, slug=slug)
    article_title = article.title
    try:
        article.delete()
        messages.success(request, "{0} has been deleted successfully".format(article_title))
    except:
        raise Http404


def logout(request):
    """Log out an active user"""
    lgout(request)
    return redirect(to="mhubblog_app:index")
