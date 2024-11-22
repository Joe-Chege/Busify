# tracker/serializers.py
from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import GPSData, SensorData, School, VehicleData

class GPSDataSerializer(DocumentSerializer):
    class Meta:
        model = GPSData
        fields = '__all__'

class SensorDataSerializer(DocumentSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class VehicleDataSerializer(DocumentSerializer):
    class Meta:
        model = VehicleData
        fields = '__all__'
