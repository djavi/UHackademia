from django.urls import path, include
from . import views
import django.views.defaults

urlpatterns = [
    path('', views.homepage, name="home"),
    path('staff/',views.staff_view,name="staff"),
    path('login/', views.login_view, name="login"),
    path('profile/', views.user_profile, name="userprofile"),
    path('rewards/', views.RewardsView.as_view(), name="rewards"),
    path('logout/', views.logout_view,name="logout")

]
