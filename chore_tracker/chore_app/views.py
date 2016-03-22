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
	'''Renders an HTML page to view the details for a housemate given a
	housemate ID'''
	housemate = get_object_or_404(Housemate, pk = housemate_id)
	return render(request, 'chore_app/detail.html', {'housemate': housemate})

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
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			post = Housemate.person.create(first_name=first_name, last_name=last_name, email=email)
			return HttpResponseRedirect('/chore_app/')
	context = {
    "form": form,
    }
	return render(request, 'chore_app/addHousemate.html', context)

def delete(request, housemate_id, chore_id):
	housemate = get_object_or_404(Housemate, pk=housemate_id)
	instance = housemate.chore_set.filter(pk=chore_id).delete()
	return HttpResponseRedirect(reverse('chore_app:detail', args=[housemate_id]))

def editInfo(request, housemate_id):
	housemate = get_object_or_404(Housemate, pk=housemate_id)
	if request.method == 'POST':
		if 'first_name' in request.POST:
			housemate.first_name = request.POST['first_name']
		if 'last_name' in request.POST:
			housemate.last_name = request.POST['last_name']
		if 'email' in request.POST:
			housemate.email = request.POST['email']
		housemate.save()
		return HttpResponseRedirect('/chore_app/')
	return render(request, 'chore_app/editInfo.html')
