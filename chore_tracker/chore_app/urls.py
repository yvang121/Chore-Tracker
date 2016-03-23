from django.conf.urls import url

from . import views

app_name = 'chore_app'

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^housemate/(?P<housemate_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^housemate/(?P<housemate_id>[0-9]+)/add_chore$', views.addChore, name='addChore'),
	url(r'^new_housemate$', views.addHousemate, name='addHousemate'),
	url(r'^housemate/(?P<housemate_id>[0-9]+)/chores/(?P<chore_id>[a-zA-Z0-9_ ]+)/delete_chore$', views.deleteChore, name='deleteChore'),
	url(r'^housemate/(?P<housemate_id>[0-9]+)/delete_housemate$', views.deleteHousemate, name='deleteHousemate'),
	url(r'^housemate/(?P<housemate_id>[0-9]+)/editInfo$', views.editInfo, name='editInfo'),
]