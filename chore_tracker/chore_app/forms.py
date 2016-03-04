from django import forms

from .models import Chore
from .models import Housemate

class ChoreForm(forms.ModelForm):
	class Meta:
		model = Chore
		fields = [
		"chore_title",
		"due_date",
		]

class HousemateForm(forms.ModelForm):
	class Meta:
		model = Housemate
		fields = [
		"first_name",
		"last_name",
		"email",
		]