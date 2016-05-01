from django.db import models
from django.forms import fields

class House(models.Model):
	''' House independent entity.'''
	house_manager = models.Manager()
	house_name = models.CharField(max_length = 200)
	zip_code = models.IntegerField(default='')

	def __str__(self):
		return self.house_name
