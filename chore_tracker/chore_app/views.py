from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone 

import datetime 
from datetime import timedelta

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
	'''Renders an HTML page to view the details for a housemate given a
	housemate ID'''
	housemate = get_object_or_404(Housemate, pk = housemate_id)
	today = datetime.datetime.date(datetime.datetime.now()) 
	tomorrow = today + timedelta(1)
	past = today - timedelta(1)
	pastweek = today - timedelta(7)  #Overdue chores will be present for 1 week.
	upcoming = tomorrow + timedelta(1)
	nextyear = today + timedelta(365)  #Upcoming chores will be present for 1 year.
	mintime = datetime.time.min
	maxtime = datetime.time.max
	current_time = datetime.datetime.time(datetime.datetime.now())
	today_set = housemate.chore_set.filter(due_date__range=(datetime.datetime.combine(today, current_time), 
		datetime.datetime.combine(today, maxtime)))
	tomorrow_set = housemate.chore_set.filter(due_date__range=(datetime.datetime.combine(tomorrow, mintime), 
		datetime.datetime.combine(tomorrow, maxtime)))
	overdue_set = housemate.chore_set.filter(due_date__range=(datetime.datetime.combine(pastweek, mintime), 
		datetime.datetime.combine(today, current_time)))
	upcoming_set = housemate.chore_set.filter(due_date__range=(datetime.datetime.combine(tomorrow, maxtime), 
		datetime.datetime.combine(nextyear, mintime)))
	context = {'housemate': housemate, 'today_set': today_set, 'tomorrow_set': tomorrow_set, 
	'overdue_set': overdue_set, 'upcoming_set': upcoming_set}
	return render(request, 'chore_app/detail.html', context)

def addChore(request, housemate_id):
	'''Creates a chore data instance for a given housemate id'''
	housemate = get_object_or_404(Housemate, pk = housemate_id)
	form = ChoreForm(request.POST or None)
	if request.method == 'POST':
		form = ChoreForm(request.POST)
		if form.is_valid():
			assigned_to = Housemate.person.get(pk=housemate_id)
			chore_title = form.cleaned_data['chore_title']
			due_date = form.cleaned_data['due_date']
			post = Chore.chore_manager.create(chore_title=chore_title, due_date=due_date, assigned_to=assigned_to)
			return HttpResponseRedirect(reverse('chore_app:detail', args=[housemate_id]))
	context = {
    'form': form,
    'housemate': housemate,
    }
	return render(request, 'chore_app/addChore.html', context)

def addHousemate(request):
	'''Creates a housemate instance'''
	form = HousemateForm(request.POST or None)
	if request.method == 'POST':
		form = HousemateForm(request.POST)
		if form.is_valid():
			first_name = form.cleaned_data['first_name'].capitalize()
			last_name = form.cleaned_data['last_name'].capitalize()
			email = form.cleaned_data['email']
			post = Housemate.person.create(first_name=first_name, last_name=last_name, email=email)
			return HttpResponseRedirect('/chore_app/')
	context = {
    "form": form,
    }
	return render(request, 'chore_app/addHousemate.html', context)

def deleteChore(request, housemate_id, chore_id):
	housemate = get_object_or_404(Housemate, pk=housemate_id)
	instance = housemate.chore_set.filter(pk=chore_id).delete()
	return HttpResponseRedirect(reverse('chore_app:detail', args=[housemate_id]))

def editInfo(request, housemate_id):
	housemate = get_object_or_404(Housemate, pk=housemate_id)
	if request.method == 'POST':
		if 'first_name' in request.POST and request.POST['first_name'] != '':
			housemate.first_name = request.POST['first_name'].capitalize()
		if 'last_name' in request.POST and request.POST['last_name'] != '':
			housemate.last_name = request.POST['last_name'].capitalize()
		if 'email' in request.POST and request.POST['email'] != '':
			housemate.email = request.POST['email']
		housemate.save()
		return HttpResponseRedirect('/chore_app/')
	return render(request, 'chore_app/editInfo.html')

def deleteHousemate(request, housemate_id):
	housemate = get_object_or_404(Housemate, pk=housemate_id).delete()
	return HttpResponseRedirect('/chore_app/')
