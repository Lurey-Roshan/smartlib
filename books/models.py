from django.db import models
from django.core.validators import FileExtensionValidator
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
'''
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
	('None','None'),
	('Comuter Engineering','Computer Engineering'),
	('MBS','MBS'),
	('BBA','BBA'),
	('MBBS','MBBS')
]
year_choice=[
	('None','None'),
	('first Year','first Year'),
	('Second Year','Second Year'),
	('First Sem','First Sem'),
	('Third Sem','Third Sem'),
	('10','10'),
]


class Book(models.Model):
	faculty=models.CharField(max_length=200, choices=faculty_choice, default='None')
	level=models.CharField(max_length=200, choices=level_choice,default='None')
	program=models.CharField(max_length=200, choices=program_choice,default='None')
	sem=models.CharField(max_length=200, choices=year_choice,default='None')
	book_name=models.CharField(max_length=255)
	edition=models.CharField(max_length=25, blank=True, null=True)
	author=models.CharField(max_length=100)
	published_By=models.CharField(max_length=100, blank=True)
	cover_pic=models.ImageField(upload_to='image/', default='image/pdf.png')
	file=models.FileField(upload_to='uploads/',validators=[FileExtensionValidator( ['pdf'] )])
	def __str__(self):
		return self.book_name


class Program(models.Model):
	name=models.CharField(max_length=255)
	pic=models.ImageField(upload_to='image/', default='image/pdf.png')
	text=models.TextField()

	def __str__(self):
		return self.name	
#for oldquestion
def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class OldQuestion(models.Model):
	faculty=models.CharField(max_length=200, choices=faculty_choice)
	level=models.CharField(max_length=200, choices=level_choice)
	program=models.CharField(max_length=200, choices=program_choice)
	sem=models.CharField(max_length=200, choices=year_choice)
	subject=models.CharField(max_length=255)
	year=models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(2015), max_value_current_year])
	file=models.FileField(upload_to='uploads/oldquestion/',validators=[FileExtensionValidator( ['pdf'] )])

	def __str__(self):
		return self.subject

class HandsOut(models.Model):
	faculty=models.CharField(max_length=200, choices=faculty_choice)
	level=models.CharField(max_length=200, choices=level_choice)
	program=models.CharField(max_length=200, choices=program_choice)
	sem=models.CharField(max_length=200, choices=year_choice)
	subject=models.CharField(max_length=255)
	chapter=models.CharField(max_length=255)
	note_by=models.CharField(max_length=255)
	file=models.FileField(upload_to='uploads/handsout/',validators=[FileExtensionValidator( ['pdf'] )])
	def __str__(self):
		return self.subject+" | " +self.chapter
