from django.db import models
from django.forms import fields


# Create your models here.
class House(models.Model): 
	house_manager = models.Manager()
	house_name = models.CharField(max_length = 200)
	zip_code = models.IntegerField()

	def __str__(self):
		return self.house_name