from django.shortcuts import render
from django.http import HttpResponse

def dashboard(request):
	return HttpResponse('<h1>Dashboard Page !</h1>')

# Create your views here.
