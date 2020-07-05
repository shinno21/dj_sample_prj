"""dj_sample_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from tree import views as tree_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", tree_views.index),
    path("json/", tree_views.json_data),
    path("cre_dir/", tree_views.cre_dir),
    path("rep_words/<str:words>/", tree_views.rep_words),
]
