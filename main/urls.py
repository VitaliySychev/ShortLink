from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('about/', views.AboutPage, name='about'),
    path('link/', views.LinkAdd.as_view(), name='link'),
]
