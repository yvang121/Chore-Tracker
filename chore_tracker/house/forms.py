from django import forms

from .models import House

class HouseForm(forms.Form):
	class Meta:
		model = House
		fields = [
		"house_name",
		"zip_code",
		]
	house_name = forms.CharField(max_length = 200)
	zip_code = forms.IntegerField()
