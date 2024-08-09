from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
   content="<html><body><h1>My blog</h1></body></html>" 
   return HttpResponse(content)