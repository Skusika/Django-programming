"""
URL configuration for my_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from blog.views import posts, glav, info_post_sign, post_info, people_name, people_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',glav),
    path('posts/', posts),
    path('posts/<int:number_post>', post_info),
    path('posts/<str:name_post>', info_post_sign),
    path('people/', people_name),
    path('people_detail/', people_info)
]
