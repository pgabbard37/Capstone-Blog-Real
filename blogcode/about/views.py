from django.shortcuts import render
from .models import About
from django.http import HttpResponse

def about(request):


    return render(request, 'about/about_page.html')

# Create your views here.
