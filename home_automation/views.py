from rest_framework import viewsets

from home_automation.models import Sensor
from home_automation.serializers import SensorSerializer


class SensorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Sensors to be viewed or created.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
