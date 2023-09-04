from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def home(request):
    return render(request, 'index.html')

# def home(request):
#     return HttpResponse('<h1> This is h1 tag </h1>')

