from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'generator/home.html') # third arg for whatever we want to pass with request to the html file

def password(request):
    return render(request, 'generator/password.html')