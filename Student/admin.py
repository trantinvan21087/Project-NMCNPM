from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Classes)
admin.site.register(Student)
admin.site.register(ClassList)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Score)