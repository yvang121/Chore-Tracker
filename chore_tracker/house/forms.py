from django import forms

from .models import House


class HouseForm(forms.Form):
	''' Defines the form to show up on the page of adding a house
		Requires house name and zip code '''
	class Meta:
		model = House
		fields = [
		"house_name",
		"zip_code",
		]
	house_name = forms.CharField(max_length = 200)
	zip_code = forms.IntegerField()
