from django.db import models

# Create your models here.
class AboutUS(models.Model):
	text=models.TextField()

	def __str__(self):
		return self.text[:20]


class OurTeam(models.Model):
	name=models.CharField(max_length=255)
	designation=models.CharField(max_length=255)
	pic=models.ImageField(upload_to='team/', default='team/man.png')

	def __str__(self):
		return self.name

class OurCient(models.Model):
	logo=models.ImageField(upload_to='client')
	name=models.CharField(max_length=255)
	link=models.CharField(max_length=255)
	address=models.CharField(max_length=255)
	text=models.TextField()

	def __str__(self):
		return self.name