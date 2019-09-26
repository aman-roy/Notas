from napp import views
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r"^logout/$", views.logout_request, name="logout"),
    url(r"^login/$", views.login_user, name="login"),
]