from django.conf.urls import url

from . import views

app_name = 'house'

urlpatterns = [
url(r'^$', views.HouseView.as_view(), name='house'),
]