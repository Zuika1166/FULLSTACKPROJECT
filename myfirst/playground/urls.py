from django.urls import path
from .import views


urlpatterns = [
    path('hello/', views.say_hello),
    path('home/', views.home),
    path('about/', views.about),
    path('portfolio/', views.registerPage),
    path('login/', views.login),
    path('singin/', views.singin),
]
