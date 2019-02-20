"""movie_app URL Configuration

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
from django.urls import path, include

urlpatterns = [
    #include allows us to reference other URLconfs (like this one)
    # it chops off of the part of the url that has matched so far and passes the other half to the other URLconf (here it passes it to 'movies/urls.py')
    path('movies/', include('movies.urls')),
    path('admin/', admin.site.urls), #we don't have to use include only for the admin urls 
]
