# myfrontend/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='google'),
    path('input/', views.text_input_view, name='text_input'),
    
    path('sign-in/', views.sign_in_view, name='sign_in')
]