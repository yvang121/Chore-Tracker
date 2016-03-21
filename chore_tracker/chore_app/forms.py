from django import forms
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
import datetime

from .models import Chore
from .models import Housemate

class ChoreForm(forms.Form):
	class Meta:
		model = Chore
		fields = [
		"chore_title",
		"due_date",
		]

	chore_title = forms.CharField(max_length = 200)
	due_date = forms.DateTimeField(widget=DateTimeWidget(bootstrap_version=3), initial = datetime.datetime.now, 
		input_formats = ['%d/%m/%Y %H:%M'])


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
