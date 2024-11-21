from django.db import models
import datetime


class GPSData(models.Model):
    device_id = models.CharField(max_length=100)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    timestamp = models.DateTimeField(auto_now_add=True)

class ShapefileData(models.Model):
    name = models.CharField(max_length=100)

class SensorData(models.Model):
    device_id = models.CharField(max_length=100)
    acceleration = models.JSONField()
    gyroscope = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)

class VehicleData(models.Model):
    device_id = models.CharField(max_length=100)
    location = models.JSONField()  # Replacing PointField with JSONField
    timestamp = models.DateTimeField(default=datetime.datetime.utcnow)

    def __str__(self):
        return f"{self.device_id} at {self.timestamp}"
    

class School(models.Model):
    name = models.CharField(max_length=200)
    location = models.JSONField()  # Replacing PointField with JSONField
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
