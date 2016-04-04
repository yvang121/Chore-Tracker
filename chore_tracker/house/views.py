from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from datetime import timedelta
from .forms import HouseForm
from .models import House

# Create your views here.
class HouseView(generic.ListView):
	template_name = 'house/house.html'
	model = House
	context_object_name = 'houses'
	
	def get_queryset(self):
		'''Return the most recent by last name'''
		return House.house_manager.order_by('house_name')

def addHouse(request):
    form = HouseForm(request.POST or None)
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            house_name = form.cleaned_data['house_name'].capitalize()
            zip_code = form.cleaned_data['zip_code']
            post = House.house_manager.create(house_name=house_name, zip_code=zip_code)
            return HttpResponseRedirect('/house/')
    context = {'form': form,
    }
    return render(request, 'house/addHouse.html', context)

def deleteHouse(request, house_id):
    house = get_object_or_404(House, pk=house_id).delete()
    return HttpResponseRedirect('/house')

def editHouse(request, house_id):
    house = get_object_or_404(House, pk=house_id)
    if request.method == 'POST':
        if 'house_name' in request.POST and request.POST['house_name'] != '':
            house.house_name = request.POST['house_name'].capitalize()
        if 'zip_code' in request.POST and request.POST['zip_code'] != '':
            house.zip_code = request.POST['zip_code'].capitalize()
        housemate.save()
        return HttpResponseRedirect('/house')
    return render(request, 'house/editHouse.html')

