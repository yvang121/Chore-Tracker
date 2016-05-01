from django import forms

from .models import House

''' House form that allows users to add a house by typing in a
house name/address and ZIP code. (All are currently required)  
'''
class HouseForm(forms.Form):
	
	class Meta:
		model = House
		fields = [
		"house_name",
		"zip_code",
		]
	house_name = forms.CharField(max_length = 200)
	zip_code = forms.IntegerField()
