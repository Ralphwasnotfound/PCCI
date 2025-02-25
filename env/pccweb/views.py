from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    request.user
    return render(request, 'home.html')

# ABOUT PAGES
def about(request):
    return render(request, 'about/about.html')

def contact(request):
    return render(request, 'about/contact.html')

def personels(request):
    return render(request, 'about/personels.html')
# Personels Pages
def administration(request):
    return render(request, 'about/personels/administration.html')

def administrative(request):
    return render(request, 'about/personels/administrative-staff.html')

def board(request):
    return render(request, 'about/personels/board.html')

def deans(request):
    return render(request, 'about/personels/deans.html')

def fulltime(request):
    return render(request, 'about/personels/full-time.html')

def parttime(request):
    return render(request, 'about/personels/part-time.html')

def SHS(request):
    return render(request, 'about/personels/SHS.html')

# Gallery

def gallery(request):
    return render(request, 'about/gallery.html')

#Navtabs

def admission(request):
    return render(request, 'navtab/admission.html')

#  Navtabs/Admission

def basicEducation(request):
    return render(request, 'navtab/admission/basiceducation.html')

def college(request):
    return render(request, 'navtab/admission/college.html')

# ACADEMICS/COLLEGE

def BSIT(request):
    return render(request, 'academics/college/BSIT.html')

def ACT(request):
    return render(request, 'academics/college/ACT.html')

def BSBA(request):
    return render(request, 'academics/college/BSBA.html')

def BSCRIM(request):
    return render(request, 'academics/college/BSCRIM.html')

# ACADEMICS/Basic education

def JRHIGH(request):
    return render(request, 'academics/basicedu/jrhigh.html')

def SRHIGH(request):
    return render(request, 'academics/basicedu/srhigh.html')

# ACADEMIC PAGE

def ACADS(request):
    return render(request, 'academics/academics.html')

# PROGRAMS

def collegeprog(request):
    return render(request, 'programs/college/college-prog.html')

def basiceduprog(request):
    return render(request, 'programs/basicedu/basicedu-prog.html')

def tesdaprog(request):
    return render(request, 'programs/tesda/tesda-prog.html')

# PORTALS
def portal(request):
    return render(request, 'portals/portal.html')

def collegeportal(request):
    return render(request, 'portals/college/collegeportal.html')

def basiceduportal(request):
    return render(request, 'portals/basiceducation/basiceduportal.html')

# RESOURCES

def SMS(request):
    return render(request, 'student-hub/student-resources/SMS.html')

def AC(request):
    return render(request, 'student-hub/student-resources/academic-calendar.html')

# STUDENT AFFAIRS

def TSF(request):
    return render(request, 'student-hub/student-affairs/TSF.html')

def studentorg(request):
    return render(request, 'student-hub/student-affairs/studentorg.html')

def decipline(request):
    return render(request, 'student-hub/student-affairs/studentdecipline.html')

# SERVICES

def library(request):
    return render(request, 'student-hub/student-services/library.html')

def registrar(request):
    return render(request, 'student-hub/student-services/registrar.html')

