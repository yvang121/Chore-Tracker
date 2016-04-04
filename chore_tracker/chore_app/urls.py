from django.conf.urls import url, include
from django.contrib import admin

from . import views

app_name = 'chore_app'

urlpatterns = [
	url(r'^$',views.home,name='home'),
	url(r'^(?P<house_id>[0-9]+)/home/$', views.index, name='index'),
	url(r'^house/(?P<house_id>[0-9]+)/housemate/(?P<housemate_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^house/(?P<house_id>[0-9]+)/housemate/(?P<housemate_id>[0-9]+)/add_chore$', views.addChore, name='addChore'),
	url(r'^(?P<house_id>[0-9]+)/new_housemate$', views.addHousemate, name='addHousemate'),
	url(r'^house/(?P<house_id>[0-9]+)/housemate/(?P<housemate_id>[0-9]+)/chores/(?P<chore_id>[a-zA-Z0-9_ ]+)/delete_chore$', views.deleteChore, name='deleteChore'),
	url(r'^house/(?P<house_id>[0-9]+)/housemate/(?P<housemate_id>[0-9]+)/delete_housemate$', views.deleteHousemate, name='deleteHousemate'),
	url(r'^house/(?P<house_id>[0-9]+)/housemate/(?P<housemate_id>[0-9]+)/editInfo$', views.editInfo, name='editInfo'),
	# Registration
	# visit /accounts/register/ to register
	# login at /accounts/login/
	url(r'^accounts/', include('registration.backends.simple.urls')),

]
