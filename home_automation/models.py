# stdlib
import uuid

# third-party imports
from django.db import models

class Sensor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    device_id = models.UUIDField()
    device_name = models.TextField()
    temperature = models.PositiveIntegerField()
    humidity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s %s %s %s' % (self.id, self.device_id, self.device_name, self.temperature, self.humidity)
