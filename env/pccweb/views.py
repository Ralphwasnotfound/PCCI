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
