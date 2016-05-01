from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from datetime import timedelta
from .forms import HouseForm
from .models import House

@login_required()
def houseView(request):
    ''' Renders an HTML page to view all houses.'''
    house_list = House.house_manager.order_by('house_name')
    #Search Bar
    query = request.GET.get("q")
    if query:
        house_list = house_list.filter(house_name__icontains=query)
    context = {'houses': house_list}
    return render(request, 'house/house.html', context)

@login_required()
def addHouse(request):
    '''Renders an HTML page to add a house.'''
    form = HouseForm(request.POST or None)
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            house_name = form.cleaned_data['house_name'].title()
            zip_code = form.cleaned_data['zip_code']
            post = House.house_manager.create(house_name=house_name, zip_code=zip_code)
            return HttpResponseRedirect('/house/')
    context = {'form': form}
    return render(request, 'house/addHouse.html', context)

@login_required()
def deleteHouse(request, house_id):
    '''Renders an HTML page to delete a house given a house ID'''
    house = get_object_or_404(House, pk=house_id).delete()
    return HttpResponseRedirect('/house')

@login_required()
def editHouse(request, house_id):
    '''Renders an HTML page to edit information of a house given a house ID'''
    house = get_object_or_404(House, pk=house_id)
    if request.method == 'POST':
        if 'house_name' in request.POST:
            house.house_name = request.POST['house_name'].title()
        if 'zip_code' in request.POST:
            house.zip_code = request.POST['zip_code'].title()
        house.save()
        return HttpResponseRedirect(reverse('chore_app:houseSummary', args=[house_id]))
    context = {'house': house}
    return render(request, 'house/editHouse.html', context)

