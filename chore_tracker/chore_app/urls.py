from django.conf.urls import url, include
from django.contrib import admin

from . import views

app_name = 'chore_app'

urlpatterns = [
	url(r'^$',views.home,name='home'),
	url(r'^house/(?P<house_id>[0-9]+)/$', views.houseSummary, name='houseSummary'),
	url(r'^house/(?P<house_id>[0-9]+)/add_housemate$', views.addHousemate, name='addHousemate'),
	url(r'^house/(?P<house_id>[0-9]+)/housemate/(?P<housemate_id>[0-9]+)/summary$', views.choreSummary, name='choreSummary'),
	url(r'^house/(?P<house_id>[0-9]+)/housemate/(?P<housemate_id>[0-9]+)/add_chore$', views.addChore, name='addChore'),
	url(r'^house/(?P<house_id>[0-9]+)/housemate/(?P<housemate_id>[0-9]+)/chores/(?P<chore_id>[a-zA-Z0-9_ ]+)/delete_chore$', views.deleteChore, name='deleteChore'),
	url(r'^house/(?P<house_id>[0-9]+)/housemate/(?P<housemate_id>[0-9]+)/delete_housemate$', views.deleteHousemate, name='deleteHousemate'),
	url(r'^house/(?P<house_id>[0-9]+)/housemate/(?P<housemate_id>[0-9]+)/editHousemate$', views.editHousemate, name='editHousemate'),
]
