import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class StudentFilter(django_filters.FilterSet):
	name = CharFilter(field_name='name', lookup_expr='icontains')


	class Meta:
		model = Student
		fields = ['name']