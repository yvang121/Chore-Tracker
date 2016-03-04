from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .forms import ChoreForm, HousemateForm
from .models import Housemate, Chore

class IndexView(generic.ListView):
	'''Displays a generic display for a particular object. The input
	needs to know the model attribute in order to do so. Ideally, this
	function will display a list of housemate names, wherein a user can click
	on the housemate name link that will lead to a list of chores for that
	housemate.
	'''
	template_name = 'chore_app/index.html'
	model = Housemate
	context_object_name = 'alphabetical_order'
	
	def get_queryset(self):
		'''Return the most recent by last name'''
		return Housemate.person.order_by('last_name')

def detail(request, housemate_id):
	housemate = get_object_or_404(Housemate, pk = housemate_id)
	return render(request, 'chore_app/detail.html', {'housemate': housemate})

def addChore(request, housemate_id):
	housemate = get_object_or_404(Housemate, pk = housemate_id)
	form = ChoreForm(request.POST or None)
	context = {
    "form": form,
    }
	return render(request, 'chore_app/addChore.html', context)
	#{'housemate': housemate}

def addHousemate(request):
	form = HousemateForm(request.POST or None)
	context = {
    "form": form,
    }
	return render(request, 'chore_app/addHousemate.html', context)