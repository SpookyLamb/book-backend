"""
URL configuration for project_auth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from catalog_app.views import *
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', get_profile),
    path('token/', TokenObtainPairView.as_view()),
    path('create-user/', create_user),
    path('create-book/', create_book),
    path('get-books/', get_books),
    path('edit-book/', edit_book),
    path('', include(router.urls)),
]