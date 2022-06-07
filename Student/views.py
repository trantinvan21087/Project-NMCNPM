import requests
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

from .filters import StudentFilter

@login_required(login_url='login')
@admin_only
def home(request):
	return redirect('/admin')

def studentList(request):
	return HttpResponse('studentList')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Student'])
def studentProfile(request):
	scores = request.user.Student.score_set.all()
	for i in scores:
		if i.semester == 'học kỳ 1':
			hk1 = i
		else:
			hk2 = i
	print(hk1.Toan)
	context = {'hk1':hk1,'hk2':hk2}
	return render(request,"Student/studentProfile.html",context)

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

			Student.objects.create(
				user=user,
				name=user.username,
				)

			Score.objects.create(
				students = user.Student,
				semester = "học kỳ 1",
				)
			Score.objects.create(
				students = user.Student,
				semester = "học kỳ 2",
				)

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
	students = Student.objects.all()
	avgScores1 = []
	avgScores2 = []

	myFilter = StudentFilter(request.GET, queryset=students)
	students = myFilter.qs 

	for i in students:
		temp = i.score_set.all()
		for j in temp:
			if j.semester == 'học kỳ 1':
				avgScores1.append(AvgScore(j))
			else:
				avgScores2.append(AvgScore(j))
				
	context = {'students':students,'avgScores1':avgScores1,'avgScores2':avgScores2,'myFilter':myFilter}
	return render(request, 'Student/searchStudent.html',context)

def createClass(request):
	return HttpResponse('createClass')

def editScore(request):
	return render(request, 'Student/editScore.html')

def createListStudent(request):
	print(request)
	return render(request, 'Student/createListStudent.html')

def teacherReport(request):
	return HttpResponse('teacherReport')

def changeRule(request):
	return HttpResponse('changeRule')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Student'])
def accountSettings(request):
	user = request.user.Student
	form = CustomerForm(instance=user)

	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES,instance=user)
		if form.is_valid():
			form.save()
			return redirect('studentProfile')


	context = {'form':form}
	return render(request, 'Student/account_setting.html', context)