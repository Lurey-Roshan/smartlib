from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	is_account_verified=models.BooleanField(default=False)
	is_student=models.BooleanField(default=True)
	is_administrator=models.BooleanField(default=False)
	

	def __str__(self):
		return self.username