from django.db import models
from django.forms import fields


# Create your models here.
class House(models.Model):
	''' Defines the house model
		Requires house name and zip code'''
	house_manager = models.Manager()
	house_name = models.CharField(max_length = 200)
	zip_code = models.IntegerField(default='')

	def __str__(self):
		return self.house_name
