from django.conf import settings
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
import requests
from decouple import config

# weather class view
class WeatherDetailsView(APIView):
    def post(self, request):
        
        weather_key = settings.WEATHER_KEY
        
        city = request.data.get('city_name')

        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}'

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp_kelvin = data['main']['temp']
            temp_celsius = temp_kelvin - 273.15
            desc = data['weather'][0]['description']
            return Response(f'{city} current temperature is: {temp_celsius:.2f}°C. {desc}')
        else:
            return Response({"Message":"Please Enter The valid city name"},status=status.HTTP_400_BAD_REQUEST)
