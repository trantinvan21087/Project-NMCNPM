from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('You are not authorized to view this page')
		return wrapper_func
	return decorator

def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'Student':
			return redirect('studentProfile')

		if group == 'Teacher':
			instance = request.user.Teacher.classes.all()[0].name
			return redirect('createListStudent',curClasses = instance)

		if group == 'admin':
			return view_func(request, *args, **kwargs)

	return wrapper_function	