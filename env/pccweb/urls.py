from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # ABOUT PAGES
    path('PCC/', views.pcc, name='PCC'),
    
]