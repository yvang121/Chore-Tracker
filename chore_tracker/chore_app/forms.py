from django import forms
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
import datetime

from .models import Chore
from .models import Housemate


''' Chore form that allows users to add a chore by typing in a
chore title and selecting a date and time. (All are currently required)  
'''

class ChoreForm(forms.Form):
	class Meta:
		model = Chore
		fields = [
		"chore_title",
		"due_date",
		]

	dateTimeOptions = {
	'format': 'mm/dd/yyyy HH:ii P',  #Formats date and time. 
	'autoclose': True, 
	'showMeridian' : True,   #Shows 12 hour time (AM and PM)
	}

	widgets = {
	'datetime': DateTimeWidget(options = dateTimeOptions)
	}

	chore_title = forms.CharField(max_length = 200)


	due_date = forms.DateTimeField(widget=DateTimeWidget(bootstrap_version=3, options=dateTimeOptions),
		input_formats = ['%m/%d/%Y %I:%M %p'])
	

''' Housemate form that allows users to add a housemate by typing in a first name, last
name and email address.  (All are currently required)   
'''

class HousemateForm(forms.Form):
	class Meta:
		model = Housemate
		fields = [
		"first_name",
		"last_name",
		"email",
		]
	first_name = forms.CharField(max_length = 100)
	last_name = forms.CharField(max_length = 100)
	email = forms.EmailField(max_length = 300)

