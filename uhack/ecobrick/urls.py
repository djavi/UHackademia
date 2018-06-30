from django.urls import path, include
from . import views
import django.views.defaults
urlpatterns = [
    path('', views.HomeView.as_view(), name="home")
]
