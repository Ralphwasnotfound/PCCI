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

    # ACADEMICS/COLLEGE

    path('academics/college/computer-studies', views.BSIT, name='BSIT'),

    path('academics/college/associate-in-computer', views.ACT, name='ACT'),

    path('academics/college/business-administration', views.BSBA, name='BSBA'),

    path('academics/college/criminology', views.BSCRIM, name='BSCRIM'),

    # ACADEMICS/Basic Education

    path('academics/basicedu/junior-high-school', views.JRHIGH, name='JRHIGH'),

    path('academics/basicedu/senior-high-school', views.SRHIGH, name='SRHIGH'),

    # ACADEMIC PAGE
    path('academics/', views.ACADS, name='academics'),

    # Programs

    path('programs/college/', views.collegeprog, name='college-prog'),

    path('programs/basic-education/', views.basiceduprog, name='basic-prog'),

    path('programs/tesda/', views.tesdaprog, name='tesda-prog'),

    # Portals

    path('portals/', views.portal, name='portal'),

    path('portal/college/', views.collegeportal, name='collegeportal'),

    path('portal/basic-education/', views.basiceduportal, name='basiceduportal'),

    # RESOURCES

    path('student-hub/resources/student-management-system/', views.SMS, name='SMS'),
    
    path('student-hub/resources/academic-calendar/', views.AC, name='AC'),


    # STUDENT AFFAIRS

    path('student-hub/student-affairs/tuition-fee,scholarships-and-financial-aids/', views.TSF, name='TSF'),

    path('student-hub/student-affairs/student-org/', views.studentorg, name='student-org'),

    path('student-hub/student-affairs/student-decipline/', views.decipline, name='decipline'),

    # SERVICES

    path('student-hub/student-services/library/', views.library, name='library'),

    path('student-hub/student-services/rigistrar/', views.registrar, name='registrar'),

]