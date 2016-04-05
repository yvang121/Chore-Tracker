from django.contrib import admin

from .models import Housemate, Chore

'''In order to view the chores associated to each Housemate in the 
admin page, you have to specify a Chore Admin class that will 
structurally display that information, like below states.
'''
class ChoreInline(admin.TabularInline):
	model = Chore
	extra = 3

class HousemateAdmin(admin.ModelAdmin):
	fieldsets = [
	(None,		{'fields':['first_name', 'last_name', 'house']}),
	('Email information', {'fields':['email'], 'classes':['collapse']}),
	]
	inlines = [ChoreInline]
	search_fields = ['first_name', 'last_name', 'email']


admin.site.register(Housemate, HousemateAdmin)
