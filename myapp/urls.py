from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.contrib.auth import views as auth_views


# class RegisterView:
#     @classmethod
#     def as_view(cls):
#         pass


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout', auth_views.LogoutView.as_view(), name="logout"),
    path('index', views.index, name="index"),
    path('about', views.about, name="about"),
    path('services', views.services, name="services"),
    path('contact', views.contact, name="contact")
]


