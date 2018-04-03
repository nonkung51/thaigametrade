"""thaigametrade URL Configuration

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
from django.contrib.auth import views as auth_views
from .views import HomePageView, GameRequestView
from game.views import ProductListView, GameListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^product/', include('game.urls')),
    url(r'^gamerequest/$', GameRequestView.as_view(), name='gamerequest'),
    url(r'^game/$', GameListView.as_view(), name='gamelist'),
    url(r'^game/(?P<pk>\d+)/$', ProductListView.as_view(), name='game'),
    url(r'^accounts/', include('accounts.urls')),
]
