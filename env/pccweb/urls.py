from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # ABOUT PAGES
    path('about/', views.about, name='about'),

    path('contact-us/', views.contact, name='contact'),

    path('personels/', views.personels, name='personels'),

    path('gallery/', views.gallery, name='gallery'),

    # Navtabs

    path('admission/', views.admission, name='admission'),

    # Navtabs/Admission

    path('admission/basic-education', views.basicEducation, name='basicEducation'),

    path('admission/college', views.college, name='college'),



]