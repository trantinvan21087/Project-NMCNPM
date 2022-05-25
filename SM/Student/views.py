from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	return render(request,"SM/dashboard.html")

def studentList(request):
	return HttpResponse('studentList')

def studentProfile(request):
	return HttpResponse('studentProfile')

def Login(request):
	return HttpResponse('studentProfile')

def acceptStudent(request):
	return HttpResponse('studentProfile')

def searchStudent(request):
	return HttpResponse('studentProfile')

def createClass(request):
	return HttpResponse('studentProfile')

def studentPoint(request):
	return HttpResponse('studentProfile')

def teacherReport(request):
	return HttpResponse('studentProfile')

def changeRule(request):
	return HttpResponse('studentProfile')