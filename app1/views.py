from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_string1(request):
    return HttpResponse('<h1><marquee> this is my First String</marquee></h1>')
