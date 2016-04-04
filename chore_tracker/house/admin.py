from django.contrib import admin

# Register your models here.
from .models import House
from chore_app.models import Housemate

class HousemateInline(admin.TabularInline):
    model = Housemate
    extra = 2

class HouseAdmin(admin.ModelAdmin):
    fieldsets = [
    (None,      {'fields':['house_name', 'zip_code']}),
    ]
    inlines = [HousemateInline]
    search_fields = ['house_name', 'zip_code', 'housemate.full_name']

admin.site.register(House, HouseAdmin)
