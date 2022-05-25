from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import *
from .form import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
	return render(request,"Student/dashboard.html")

def studentList(request):
	return HttpResponse('studentList')

def studentProfile(request):
	return HttpResponse('studentProfile')

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'Student/login.html', context)

def register(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request,'Account was created for ' + user)
				return redirect('login')
		context = {'form':form }
		return render(request, 'Student/register.html',context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def acceptStudent(request):
	return HttpResponse('Login')

def searchStudent(request):
	return HttpResponse('searchStudent')

def createClass(request):
	return HttpResponse('createClass')

def studentPoint(request):
	return HttpResponse('studentPoint')

def teacherReport(request):
	return HttpResponse('teacherReport')

def changeRule(request):
	return HttpResponse('changeRule')