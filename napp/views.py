from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from napp.models import Author

# Create your views here.
def index(request):
	if request.user.is_authenticated:
		return render(request, 'index.html')
	return render(request, 'home.html')


def about(request):
	return render(request, 'home.html')


def contact(request):
	return render(request, 'contact.html')

def logout_request(request):
    logout(request)
    return redirect("index")