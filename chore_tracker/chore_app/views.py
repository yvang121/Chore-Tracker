from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone 
import datetime
from datetime import timedelta
from .forms import ChoreForm, HousemateForm
from .models import Housemate, Chore
from house.models import House


def home(request):
	'''Renders the HTML page that views the login and register form and the Chore Tracker greeting.'''
	return render(request, "chore_app/home.html")

@login_required()
def index(request, house_id):
	'''Renders the HTML page that views the housemates for a given house.'''
	house = get_object_or_404(House, pk=house_id)
	housemates = house.housemate_set.all()
	context = {
	'housmates': housemates, 
	'house': house,
	}
	return render(request, 'chore_app/index.html', context)

@login_required()
def choreSummary(request, house_id, housemate_id):
	'''Renders an HTML page to view the details for a housemate given a housemate ID.'''
	house = get_object_or_404(House, pk=house_id)
	housemate = get_object_or_404(Housemate, pk = housemate_id)

	'''Variables for specific dates for today, tomorrow, yesterday and the day after tomorrow.'''
	today = datetime.datetime.date(datetime.datetime.now()) 
	tomorrow = today + datetime.timedelta(1)
	past = today - datetime.timedelta(1)
	upcoming = tomorrow + datetime.timedelta(1)

	'''Variables for specific times including the current time, earliest time (0:0), latest time (23:59).'''
	current_time = datetime.datetime.time(datetime.datetime.now())
	mintime = datetime.time.min
	maxtime = datetime.time.max

	'''Variables for chore sets including the overdue set, today set, tomorrow set and upcoming set.  Each set is 
	a filtered set of a housemate's chores based on specific dates and times.'''
	overdue_set = housemate.chore_set.filter(due_date__lte=(datetime.datetime.combine(today, current_time)))
	today_set = housemate.chore_set.filter(due_date__range=(datetime.datetime.combine(today, current_time), 
		datetime.datetime.combine(today, maxtime)))
	tomorrow_set = housemate.chore_set.filter(due_date__range=(datetime.datetime.combine(tomorrow, mintime), 
		datetime.datetime.combine(tomorrow, maxtime)))
	upcoming_set = housemate.chore_set.filter(due_date__gte=(datetime.datetime.combine(tomorrow, maxtime)))

	context = {
	'housemate': housemate, 
	'today_set': today_set, 
	'tomorrow_set': tomorrow_set, 
	'overdue_set': overdue_set, 
	'upcoming_set': upcoming_set, 
	'house': house,
	}
	return render(request, 'chore_app/choreSummary.html', context)

@login_required()
def addChore(request, house_id, housemate_id):
	'''Creates a chore data instance for a given housemate ID.'''
	house = get_object_or_404(House, pk=house_id)
	housemate = get_object_or_404(Housemate, pk = housemate_id)

	'''Passes Chore Form to HTML page.'''
	form = ChoreForm(request.POST or None)
	if request.method == 'POST':
		form = ChoreForm(request.POST)
		if form.is_valid():
			'''Clean input data and assign chore to housemate.'''
			assigned_to = Housemate.person.get(pk=housemate_id)
			chore_title = form.cleaned_data['chore_title']
			due_date = form.cleaned_data['due_date']
			post = Chore.chore_manager.create(chore_title=chore_title, due_date=due_date, assigned_to=assigned_to)
			return HttpResponseRedirect(reverse('chore_app:choreSummary', args=[house_id, housemate_id]))

	context = {
    'form': form,
    'housemate': housemate,
    'house': house,
    }
	return render(request, 'chore_app/addChore.html', context)

@login_required()
def addHousemate(request, house_id):
	'''Creates a housemate instance for a given house ID.'''
	house = get_object_or_404(House, pk=house_id)

	'''Passes Housemate Form to HTML page.'''
	form = HousemateForm(request.POST or None)
	if request.method == 'POST':
		form = HousemateForm(request.POST)
		if form.is_valid():
			'''Clean input data and assign housemate to house.'''
			first_name = form.cleaned_data['first_name'].title()
			last_name = form.cleaned_data['last_name'].title()
			email = form.cleaned_data['email']
			post = Housemate.person.create(house=house, first_name=first_name, last_name=last_name, email=email)
			return HttpResponseRedirect(reverse('chore_app:index', args=[house_id]))
	context = {
	'form': form, 
	'house': house
    }
	return render(request, 'chore_app/addHousemate.html', context)

@login_required()
def deleteChore(request, house_id, housemate_id, chore_id):
	'''Takes a chore ID to delete chore, that belongs to a housemate'''
	house = get_object_or_404(House, pk=house_id)
	housemate = get_object_or_404(Housemate, pk=housemate_id)
	instance = housemate.chore_set.filter(pk=chore_id).delete()
	return HttpResponseRedirect(reverse('chore_app:choreSummary', args=[house_id, housemate_id]))

@login_required()
def editHousemate(request, house_id, housemate_id):
	'''Takes an Http request, and a housemate id to edit housemate info.'''
	house = get_object_or_404(House, pk=house_id)
	housemate = get_object_or_404(Housemate, pk=housemate_id)
	if request.method == 'POST':
		'''Reassign new data input to housemate fields.'''
		if 'first_name' in request.POST:
			housemate.first_name = request.POST['first_name'].title()
		if 'last_name' in request.POST:
			housemate.last_name = request.POST['last_name'].title()
		if 'email' in request.POST:
			housemate.email = request.POST['email']
		housemate.save()
		return HttpResponseRedirect(reverse('chore_app:index', args=[house_id]))
	context = {
	'housemate': housemate,
	'house': house,
	}
	return render(request, 'chore_app/editHousemate.html', context)

@login_required()
def deleteHousemate(request, house_id, housemate_id):
	'''Deletes a housemate, given housemate ID'''
	house = get_object_or_404(House, pk=house_id)
	housemate = get_object_or_404(Housemate, pk=housemate_id).delete()
	context = {
	'house': house,
	'housemate': housemate,
	}
	return HttpResponseRedirect(reverse('chore_app:index', args=[house_id]))
