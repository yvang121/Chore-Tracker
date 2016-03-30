from django.db import models

import datetime
from django.db import models
from django.utils import timezone
from django.forms import fields, PasswordInput

'''Our models include a Housemate entity, which has a dependent entity
of chores. A chore entity cannot exist independent of a housemate.
A chore entity will always be assigned to a housemate entity.
'''

class Housemate(models.Model):
	'''Housemate independent entity.'''
	person = models.Manager()
	first_name = models.CharField(max_length = 40)
	last_name = models.CharField(max_length = 40)
	email = models.EmailField(max_length = 200, default = '')

	def __str__(self):
		'''Used for administrators to turn a housemate object to a string
		by first and last name'''
		return '%s %s' % (self.first_name, self.last_name)

	full_name = property(__str__)


class Chore(models.Model):
	'''Chore dependent entity that is linked to a Housemate entity.'''
	assigned_to = models.ForeignKey(Housemate, on_delete = models.CASCADE,
		verbose_name = 'housemate responsible for completing this chore')
	chore_manager = models.Manager()
	chore_title = models.CharField(max_length = 200)
	create_date = timezone.now()
	due_date = models.DateTimeField(default = '')
	is_done = models.BooleanField('Status', default = False)

	def __str__(self):
		return self.chore_title

	class Meta:
		ordering = ['due_date']

class SignUp(models.Model):
	username = models.CharField(max_length = 120)
	email = models.EmailField()
	password1 = models.CharField(max_length = 120)
	password2 = models.CharField(max_length = 120)

	def __str__(self):
		return self.email

class Login(models.Model):
	username = models.CharField(max_length=120)
	password = models.CharField(max_length=120)