from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 

from .models import *

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']

class CustomerForm(ModelForm):
	class Meta:
		model = Student
		fields = '__all__'
		exclude = ['user']

class ScoreForm(ModelForm):
	class Meta:
		model = Score
		fields = '__all__'
		exclude = ['students','semester']