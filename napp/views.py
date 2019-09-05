from django.shortcuts import render
from django.http import HttpResponse
from napp.models import Author

# Create your views here.
def hello(request):
	return HttpResponse("<h1>HELLO</h1>")