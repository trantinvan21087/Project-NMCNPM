from django.db import models

# Create your models here.
class classes(models.Model):
	CATEGORY = (
		('10A1','10A1'),('10A2','10A2'),('10A3','10A3'),('10A4','10A4')
		,('11A1','11A1'),('11A2','11A2'),('11A3','11A3')
		,('12A1','12A1'),('12A2','12A2'),
		)
	name = models.CharField(max_length = 200, null = True, choices = CATEGORY)
	def __str__(self):
		return self.name

class Student(models.Model):
	name = models.CharField(max_length = 200, null = True)
	GIOITINH = (
		('Nam','Nam'),
		('Nu','Nu'),
		)
	sex = models.CharField(max_length = 200, null = True, choices = GIOITINH)
	birthday = models.DateField(null = True)
	email = models.CharField(max_length = 200, null = True)

	def __str__(self):
		return self.name

class ClassList(models.Model):
	classes = models.ForeignKey(classes,null = True, on_delete = models.SET_NULL)
	Students = models.ForeignKey(Student, null = True, on_delete = models.SET_NULL)
	def __str__(self):
		return self.Students.name +' '+ self.classes.name