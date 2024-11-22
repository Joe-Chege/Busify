from django.db import models
import datetime
from mongoengine import Document, StringField, PointField, DateTimeField

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

class VehicleData(Document):
    device_id = StringField(max_length=100, required=True)
    location = PointField(required=True)
    timestamp = DateTimeField(required=True)

    def __str__(self):
        return f"{self.device_id} at {self.timestamp}"
    
class School(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, blank=True)  # Allow the field to be blank

    def __str__(self):
        return self.name