from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Level(models.Model):
	name=models.CharField(max_length=25)
	def __str__(self):
		return self.name


class Faculty(models.Model):
	name=models.CharField(max_length=25)
	level=models.ForeignKey(Level,on_delete=models.SET_NULL,blank=True, null=True)
	def __str__(self):
		return self.name

class Program(models.Model):
	prgm=models.CharField(max_length=50)
	faculty=models.ForeignKey(Faculty,on_delete=models.SET_NULL,blank=True, null=True)
	level=models.ForeignKey(Level,on_delete=models.SET_NULL,blank=True, null=True)
	def __str__(self):
		return self.prgm

class Semester(models.Model):
	name=models.CharField(max_length=100)
	program=models.ForeignKey(Program,on_delete=models.SET_NULL,blank=True, null=True)
	faculty=models.ForeignKey(Faculty,on_delete=models.SET_NULL,blank=True, null=True)
	level=models.ForeignKey(Level,on_delete=models.SET_NULL,blank=True, null=True)
	def __str__(self):
		return self.name


class Book(models.Model):

	level=models.ForeignKey(Level,on_delete=models.SET_NULL, blank=True, null=True)
	faculty= models.ForeignKey(Faculty,on_delete=models.SET_NULL,blank=True, null=True)
	program=models.ForeignKey(Program,on_delete=models.SET_NULL, blank=True, null=True)
	sem=models.ForeignKey(Semester,on_delete=models.SET_NULL, blank=True, null=True)

	book_name=models.CharField(max_length=255)
	edition=models.CharField(max_length=25, blank=True, null=True)
	author=models.CharField(max_length=100)
	published_By=models.CharField(max_length=100, blank=True)
	cover_pic=models.ImageField(upload_to='image/', default='image/pdf.png')
	file=models.FileField(upload_to='uploads/', validators=[FileExtensionValidator( ['pdf'] )]) 

	def __str__(self):
		return self.book_name





'''
faculty_choice=[
	('None','None'),
	('Management','Management'),
	('Applied Science','Applied Scinece'),
	('Engineering','Engineering'),
	('Humanities','Humanities')
]
	
level_choice=[
	('None','None'),
	('Bachelors','Bachelors'),
	('Masters','Masters'),
	('+2','+2'),
	('Diploma','Diploma')


]
program_choice=[
	('Comuter Engineering','Computer Engineering'),
	('MBS','MBS'),
	('BBA','BBA'),
	('MBBS','MBBS')
]
year_choice=[
	('first Year','first Year'),
	('Second Year','Second Year'),
	('First Sem','First Sem'),
	('Third Sem','Third Sem'),
	('10','10'),
]


class Book(models.Model):
	faculty=models.CharField(max_length=200, choices=faculty_choice, default='None')
	level=models.CharField(max_length=200, choices=level_choice,default='None')
	program=models.CharField(max_length=200, choices=program_choice)
	year=models.CharField(max_length=200, choices=year_choice)
	name=models.CharField(max_length=255)
	edition=models.CharField(max_length=25, blank=True, null=True)
	author=models.CharField(max_length=100)
	published_By=models.CharField(max_length=100, blank=True)
	file=models.FileField(upload_to='uploads/')
	'''