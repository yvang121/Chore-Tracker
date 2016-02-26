from django.conf.urls import url

from . import views

app_name = 'chore_app'

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<housemate_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<housemate_id>[0-9]+)/addChore$', views.addChore, name='addChore'),
]