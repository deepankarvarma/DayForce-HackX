from django.db import models


class Register(models.Model):
	name=models.CharField(max_length=50)
	email=models.CharField(max_length=50)
	password=models.CharField(max_length=50)
	contact=models.CharField(max_length=50)
	address=models.CharField(max_length=50)
	


	def __str__(self):
		return self.name






# Create your models here.
