from django.contrib.gis.db import models
from mongoengine import Document, StringField, FloatField, PointField, DateTimeField
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

class VehicleData(Document):
    device_id = StringField(max_length=100, required=True)
    location = PointField(required=True)  # Use PointField for geospatial data
    timestamp = DateTimeField(default=datetime.datetime.utcnow)

    def __str__(self):
        return f"{self.device_id} at {self.timestamp}"
    

class School(Document):
    name = StringField(required=True, max_length=200)
    location = PointField(required=True)  # Use PointField for geospatial data
    address = StringField()

    def __str__(self):
        return self.name
