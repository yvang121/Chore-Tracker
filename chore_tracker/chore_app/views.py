from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone 
from datetime import timedelta
import datetime
from django.contrib.auth.views import password_reset_confirm
from .forms import ChoreForm, HousemateForm, LogInForm, SignUpForm
from .models import Housemate, Chore
from house.models import House

# Regsitration
def home(request):
	title = 'Welcome'
	form = LogInForm(request.POST or None)
	context = {
		"title": title,
		"form": form
	}

	if form.is_valid():
		instance = form.save(commit=False)
		username = form.cleaned_data.get("username")
		if not username:
			username = "New full name"
		instance.full_name = username
		instance.save()
		context = {
			"title": "Thank you"
		}
	return render(request, "chore_app/home.html", context)

def index(request, house_id):
	'''Renders the html page that views the housemates for a given house'''
	house = get_object_or_404(House, pk=house_id)
	housemates = house.housemate_set.all()
	context = {'housmates': housemates, 'house': house,
	}
	return render(request, 'chore_app/index.html', context)

def detail(request, house_id, housemate_id):
	'''Renders an HTML page to view the details for a housemate given a
	housemate ID'''
	house = get_object_or_404(House, pk=house_id)
	housemate = get_object_or_404(Housemate, pk = housemate_id)
	today = datetime.datetime.date(datetime.datetime.now()) 
	tomorrow = today + datetime.timedelta(1)
	past = today - datetime.timedelta(1)
	upcoming = tomorrow + datetime.timedelta(1)
	current_time = datetime.datetime.time(datetime.datetime.now())
	mintime = datetime.time.min
	maxtime = datetime.time.max
	overdue_set = housemate.chore_set.filter(due_date__lte=(datetime.datetime.combine(today, current_time)))
	today_set = housemate.chore_set.filter(due_date__range=(datetime.datetime.combine(today, current_time), 
		datetime.datetime.combine(today, maxtime)))
	tomorrow_set = housemate.chore_set.filter(due_date__range=(datetime.datetime.combine(tomorrow, mintime), 
		datetime.datetime.combine(tomorrow, maxtime)))
	upcoming_set = housemate.chore_set.filter(due_date__gte=(datetime.datetime.combine(tomorrow, maxtime)))
	context = {'housemate': housemate, 'today_set': today_set, 'tomorrow_set': tomorrow_set, 
	'overdue_set': overdue_set, 'upcoming_set': upcoming_set, 'house': house,}
	return render(request, 'chore_app/detail.html', context)

def addChore(request, house_id, housemate_id):
	'''Creates a chore data instance for a given housemate id'''
	house = get_object_or_404(House, pk=house_id)
	housemate = get_object_or_404(Housemate, pk = housemate_id)
	form = ChoreForm(request.POST or None)
	if request.method == 'POST':
		form = ChoreForm(request.POST)
		if form.is_valid():
			assigned_to = Housemate.person.get(pk=housemate_id)
			chore_title = form.cleaned_data['chore_title']
			due_date = form.cleaned_data['due_date']
			post = Chore.chore_manager.create(chore_title=chore_title, due_date=due_date, assigned_to=assigned_to)
			return HttpResponseRedirect(reverse('chore_app:detail', args=[house_id, housemate_id]))
	context = {
    'form': form,
    'housemate': housemate,
    'house': house,
    }
	return render(request, 'chore_app/addChore.html', context)

def addHousemate(request, house_id):
	'''Creates a housemate instance'''
	house = get_object_or_404(House, pk=house_id)
	form = HousemateForm(request.POST or None)
	if request.method == 'POST':
		form = HousemateForm(request.POST)
		if form.is_valid():
			first_name = form.cleaned_data['first_name'].title()
			last_name = form.cleaned_data['last_name'].title()
			email = form.cleaned_data['email']
			post = Housemate.person.create(house=house, first_name=first_name, last_name=last_name, email=email)
			return HttpResponseRedirect(reverse('chore_app:index', args=[house_id]))
	context = {"form": form, 'house': house
    }
	return render(request, 'chore_app/addHousemate.html', context)

def deleteChore(request, house_id, housemate_id, chore_id):
	'''Takes a chore_id to delete chore, that belongs to a housemate'''
	house = get_object_or_404(House, pk=house_id)
	housemate = get_object_or_404(Housemate, pk=housemate_id)
	instance = housemate.chore_set.filter(pk=chore_id).delete()
	return HttpResponseRedirect(reverse('chore_app:detail', args=[house_id, housemate_id]))

def editInfo(request, house_id, housemate_id):
	'''Takes an Http request, and a housemate id to edit housemate info'''
	house = get_object_or_404(House, pk=house_id)
	housemate = get_object_or_404(Housemate, pk=housemate_id)
	if request.method == 'POST':
		if 'first_name' in request.POST and request.POST['first_name'] != '':
			housemate.first_name = request.POST['first_name'].title()
		if 'last_name' in request.POST and request.POST['last_name'] != '':
			housemate.last_name = request.POST['last_name'].title()
		if 'email' in request.POST and request.POST['email'] != '':
			housemate.email = request.POST['email']
		housemate.save()
		return HttpResponseRedirect(reverse('chore_app:index', args=[house_id]))
	context = {
	'housemate': housemate,
	'house': house,
	}
	return render(request, 'chore_app/editInfo.html', context)

def deleteHousemate(request, house_id, housemate_id):
	'''Deletes a housemate, given housemate id'''
	house = get_object_or_404(House, pk=house_id)
	housemate = get_object_or_404(Housemate, pk=housemate_id).delete()
	context = {
	'house': house,
	'housemate': housemate,
	}
	return HttpResponseRedirect(reverse('chore_app:index', args=[house_id]))
