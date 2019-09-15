from django.shortcuts import render
from django.http import HttpResponse
from napp.models import Author

# Create your views here.
def index(request):
	return render(request, 'unauth/index.html')


def about(request):
	return render(request, 'unauth/about.html')


def contact(request):
	return render(request, 'unauth/contact.html')
