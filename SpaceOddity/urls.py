"""SpaceOddity URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from main_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^planet/(?P<planet_id>[0-9]+)', views.planet, name='planet'),
    url(r'^house/(?P<house_id>[0-9]+)', views.house, name='house'),
    url(r'^change_ownership/(?P<house_id>[0-9]+)', views.change_ownership, name='change_ownership'),
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^search/(?P<keyword>\w+)$', views.search_results, name='search_results'),
    url(r'^paypal/', include('paypal.standard.ipn.urls'))
]
