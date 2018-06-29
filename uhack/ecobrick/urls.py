from django.urls import path, include
from . import views
import django.views.defaults
urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
<<<<<<< HEAD
    path('staff/',views.staff_view,name="staff")
=======
    path('login/', views.login_view, name="login"),
>>>>>>> 2904ed9c253d683de246e709081e0d8b76511a96
]
