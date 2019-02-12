"""branchtown URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', lambda r: redirect('main:mainpage'), name='root'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('board/', include('board.urls', namespace='board')),
    path('main/', include('main.urls', namespace='main')),
    path('response/', include('response.urls', namespace='response')),
    path('survey/', include('survey.urls', namespace='survey')),
    path('tag/', include('tag.urls', namespace='tag')),
]
