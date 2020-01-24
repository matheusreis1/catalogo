"""catalogo_project URL Configuration

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
from django.urls import path, include
from django.conf.urls import url
import catalog_app
from rest_framework.routers import DefaultRouter
from catalog_app import views as catalog_app
from catalog_auth import views as catalog_auth

router = DefaultRouter()

router.register(r'api/actor', catalog_app.ActorAPI)
router.register(r'api/movie', catalog_app.MovieAPI)

urlpatterns = [
    path('admin/', admin.site.urls),
    url('auth/', include('catalog_auth.urls')),
    url(r'', include(router.urls))
]
