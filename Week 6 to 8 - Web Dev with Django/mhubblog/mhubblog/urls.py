"""mhubblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import (url, include)
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login
from mhubblog_app.views import logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # AUTHENTICATION URLS
    url(r'^login/$', login, {"template_name": "mhubblog_app/account/login.html"}, name="users-login"),
    url(r'^logout/$', logout, name="users-logout"),

    # URL redirect for mhubblog application
    url(r"",  include("mhubblog_app.urls", namespace="mhubblog_app"))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
