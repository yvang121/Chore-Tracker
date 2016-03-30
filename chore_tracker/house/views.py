from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .forms import HouseForm
from .models import House

# Create your views here.
class HouseView(generic.ListView):
	template_name = 'house/house.html'
	model = House
	context_object_name = 'alphabetical_order'
	
	def get_queryset(self):
		'''Return the most recent by last name'''
		return House.house_manager.order_by('house_name')