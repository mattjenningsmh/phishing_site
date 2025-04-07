# myfrontend/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('input/', views.text_input_view, name='text_input'),
    path('google/', views.google_view, name='google'),
    path('sign-in/', views.sign_in_view, name='sign_in')
]