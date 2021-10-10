from django.db import models

# Create your models here
class Program(models.Model):
	name=models.CharField(max_length=255)
	image=models.ImageField(upload_to='program/')
	text=models.TextField()
	def __str__(self):
		return self.name

class Mission(models.Model):
	mission= models.TextField()
	def __str__(self):
		return self.mission



class Message_from_Principal(models.Model):
	name=models.CharField(max_length=255)
	image=models.ImageField(upload_to='image/')
	text=models.TextField()
	def __str__(self):
		return self.name

class About_Us(models.Model):
	text=models.TextField()
	def __str__(self):
		return self.text[:50]



class Contact(models.Model):
	name=models.CharField(max_length=255)
	email=models.EmailField(max_length=100)
	messsage=models.TextField()

	def __str__(self):
		return self.name