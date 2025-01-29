from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # ABOUT PAGES
    path('about/', views.about, name='about'),

    path('contact-us/', views.contact, name='contact'),
    
]