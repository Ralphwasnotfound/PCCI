from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # ABOUT PAGES
    path('about/', views.about, name='about'),

    path('contact-us/', views.contact, name='contact'),

    path('personels/', views.personels, name='personels'),
    # Personels Pages
    path('personels/administration', views.administration, name='administration'),

    path('personels/administrative-staff', views.administrative, name='administrative'),

    path('personels/board-of-trustees', views.board, name='board'),

    path('personels/deans-and-department-heads', views.deans, name='deans'),

    path('personels/faculty-full-time', views.fulltime, name='full-time'),

    path('personels/faculty-part-time', views.parttime, name='part-time'),

    path('personels/senior-high-school-faculty', views.SHS, name='SHS'),
    # Gallery
    path('gallery/', views.gallery, name='gallery'),

    # Navtabs

    path('admission/', views.admission, name='admission'),

    # Navtabs/Admission

    path('admission/basic-education', views.basicEducation, name='basicEducation'),

    path('admission/college', views.college, name='college'),



]