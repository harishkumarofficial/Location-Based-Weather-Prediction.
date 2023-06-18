from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [

    path('', views.WeatherDetailsView.as_view(), name='weather-details'),
]
