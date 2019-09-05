from napp import views
from django.urls import path

urlpatterns = [
    path('', views.hello, name='index'),
]