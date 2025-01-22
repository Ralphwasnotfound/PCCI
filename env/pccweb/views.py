from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    request.user
    return render(request, 'home.html')