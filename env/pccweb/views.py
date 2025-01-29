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