from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.urls import reverse

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
    return redirect('index')

def login_user(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			login(request,user)
			messages.add_message(request, messages.INFO, 'Logged In')
		else:
			messages.add_message(request, messages.INFO, 'Invalid Data')
		return HttpResponseRedirect(reverse('index'))
	else:
		return render(request, 'index.html')

def signup(request):
	if request.method == "POST":
		fullname = request.POST.get('')
