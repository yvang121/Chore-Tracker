from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'house'

urlpatterns = [
    url(r'^$', login_required(views.HouseView.as_view()), name='house'),
    url(r'^new_house$', views.addHouse, name='addHouse'),
    url(r'^house/(?P<house_id>[0-9]+)/delete_house$', views.deleteHouse, name='deleteHouse'),
    url(r'^(?P<house_id>[0-9]+)/editHouse$', views.editHouse, name='editHouse'),
]
