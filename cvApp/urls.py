from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('about/', views.aboutPage, name='aboutPage'),
    path('resume/', views.resumePage, name='resumePage'),
    path('certif/', views.certifPage, name='certifPage'),
    path('contact/', views.contactPage, name='contactPage'),
]
