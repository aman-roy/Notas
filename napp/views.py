from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from napp.models import Notes, Author
from django.contrib.auth.models import User

# Create your views here.
def index(request):
	if request.user.is_authenticated:
		last_five = Notes.objects.all()[:5]
		last_five_in_ascending_order = reversed(last_five)
		return render(request, 'index.html', {"notes": last_five_in_ascending_order})
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def contact(request):
	return render(request, 'contact.html')

@login_required(login_url='/admin/')
def logout_request(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'Logged out')
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

@login_required(login_url='/admin/')
def search(request):
	if request.method == "POST":
		key = request.POST.get('searchVal')
		data = Notes.objects.filter(name__icontains=key)
		return render(request, 'search.html', {"data": data, "key": key})
	else:
		return HttpResponseRedirect(reverse('index'))
