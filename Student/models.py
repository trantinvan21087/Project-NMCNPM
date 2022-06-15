from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Classes(models.Model):
	CATEGORY = (
		('10A1','10A1'),('10A2','10A2'),('10A3','10A3'),('10A4','10A4')
		,('11A1','11A1'),('11A2','11A2'),('11A3','11A3')
		,('12A1','12A1'),('12A2','12A2'),
		)
	name = models.CharField(max_length = 200, null = True, choices = CATEGORY, unique = True)
	def __str__(self):
		return self.name

class Student(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE,related_name='Student')
	name = models.CharField(max_length = 200, null = True)
	GIOITINH = (
		('Nam','Nam'),
		('Nữ','Nữ'),
		)
	sex = models.CharField(max_length = 200, null = True, choices = GIOITINH)
	birthday = models.DateField(null = True)
	email = models.CharField(max_length = 200, null = True)
	house_location = models.CharField(max_length = 200, null = True)
	classes = models.ForeignKey(Classes, null = True, on_delete = models.CASCADE)
	def __str__(self):
		return self.name

class Subject(models.Model):
	SUBJECT = (
			('Toán','Toán'),('Lý','Lý'),('Hóa','Hóa')
			,('Sinh','Sinh'),('Sử','Sử'),('Địa','Địa')
			,('Văn','Văn'),('Đạo đức','Đạo đức'),('Thể dục','Thể dục'),
		)
	name = models.CharField(max_length = 200, null = True, choices = SUBJECT, unique = True)

	def __str__(self):
		return self.name

class Teacher(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE,related_name='Teacher')
	name = models.CharField(max_length = 200, null = True)
	GIOITINH = (
		('Nam','Nam'),
		('Nu','Nu'),
		)
	sex = models.CharField(max_length = 200, null = True, choices = GIOITINH)
	birthday = models.DateField(null = True)
	email = models.CharField(max_length = 200, null = True)
	SUBJECT = (
			('Toán','Toán'),('Lý','Lý'),('Hóa','Hóa')
			,('Sinh','Sinh'),('Sử','Sử'),('Địa','Địa')
			,('Văn','Văn'),('Đạo đức','Đạo đức'),('Thể dục','Thể dục'),
		)
	subject = models.CharField(max_length = 200, null = True, choices = SUBJECT, unique = True)
	classes = models.ManyToManyField(Classes)
	def __str__(self):
		return self.name

class Score(models.Model):
	SEMESTER = (
		('học kỳ 1','học kỳ 1'),('học kỳ 2','học kỳ 2')
		)
	semester = models.CharField(max_length = 200, null = True, choices = SEMESTER)
	students = models.ForeignKey(Student, null = True, on_delete = models.CASCADE)

	Toan = models.FloatField(default=0,validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
	Ly =  models.FloatField(default=0,validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
	Hoa =  models.FloatField(default=0,validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
	Sinh =  models.FloatField(default=0,validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
	Su = models.FloatField(default=0,validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
	Dia = models.FloatField(default=0,validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
	Van = models.FloatField(default=0,validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
	Daoduc = models.FloatField(default=0,validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
	TheDuc = models.FloatField(default=0,validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
	class Meta:
		unique_together = ('semester', 'students')
	def __str__(self):
		return self.students.name +' '+ self.semester

def AvgScore(Score):
	return round((float(Score.Toan) + float(Score.Ly) + float(Score.Hoa)
	 + float(Score.Sinh) + float(Score.Su) + float(Score.Dia) 
	 + float(Score.Van) + float(Score.Daoduc) + float(Score.TheDuc))/9,1)

def subjectScore(Score, name):
	if name == "Toán" : return Score.Toan
	elif name == "Lý" : return Score.Ly
	elif name == "Hóa" : return Score.Hoa
	elif name == "Sinh" : return Score.Sinh
	elif name == "Sử" : return Score.Su
	elif name == "Địa" : return Score.Dia
	elif name == "Văn" : return Score.Van
	elif name == "Đạo đức" : return Score.Daoduc
	elif name == "Thể dục" : return Score.Theduc

def subjectVar(name):
	if name == "Toán" : return 'Toan'
	elif name == "Lý" : return 'Ly'
	elif name == "Hóa" : return 'Hoa'
	elif name == "Sinh" : return 'Sinh'
	elif name == "Sử" : return 'Su'
	elif name == "Địa" : return 'Dia'
	elif name == "Văn" : return 'Van'
	elif name == "Đạo đức" : return 'Daoduc'
	elif name == "Thể dục" : return 'Theduc'