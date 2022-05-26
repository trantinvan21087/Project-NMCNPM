from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import *
from .form import *
from .decorators import *
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
@admin_only
def home(request):
	return render(request,"Student/dashboard.html")

def studentList(request):
	return HttpResponse('studentList')

def studentProfile(request):
	return render(request,"Student/studentProfile.html")

@unauthenticated_user
def loginPage(request):
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

@unauthenticated_user
def register(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='Student')
			user.groups.add(group)
			messages.success(request,'Account was created for ' + username)
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