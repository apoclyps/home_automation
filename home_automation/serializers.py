from django.contrib.auth.models import User, Group
from home_automation.models import Sensor
from rest_framework import serializers
from home_automation.fields import UUIDField


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'device_id', 'device_name', 'temperature', 'humidity', 'created_at')
