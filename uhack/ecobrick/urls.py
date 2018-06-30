from django.urls import path, include
from . import views
import django.views.defaults
urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('rewards/', views.RewardsView.as_view(), name="home")
]
