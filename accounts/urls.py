from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import (RegisterView, ProfileEditView,
                    ProfileDetailView,)

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^register/$',RegisterView.as_view(), name='register'),
    url(r'^edit/(?P<pk>\d+)/$',ProfileEditView.as_view(), name='profile_edit'),
    url(r'^profile/(?P<pk>\d+)/$',ProfileDetailView.as_view(), name='profile'),
]
