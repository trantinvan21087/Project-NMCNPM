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
		exclude = ['user','classes']

class ScoreForm(ModelForm):
	def __init__(self, *args, **kwargs):
		subject = kwargs.pop('subject')
		super(ScoreForm, self).__init__(*args, **kwargs)
		temp = self.fields.copy()
		for i in temp:
			if not i == subject:
				self.fields.pop(i)
	class Meta:
		model = Score
		fields = '__all__'
		exclude = ['students','semester']

# class RandomForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(RandomForm, self).__init__(*args, **kwargs)
#         if not self.instance:
#             self.fields.pop('active')

#     class Meta:
#         model = models.Service
#         fields = (...some fields...)