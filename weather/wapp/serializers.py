from rest_framework import serializers
from .models import Weather, City, Subscribed


class CitiesWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class SubscribedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribed
        fields = "__all__"
