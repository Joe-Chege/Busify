from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from pymongo import MongoClient
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_mongoengine import generics
from rest_framework import generics as drf_generics
from .models import GPSData, SensorData, VehicleData, School
from .serializers import GPSDataSerializer, SensorDataSerializer, SchoolSerializer, VehicleDataSerializer
import json
import datetime
from rest_framework import status
from rest_framework.views import APIView

def gps_data_view(request):
    gps_data = GPSData.objects.all().values('device_id', 'latitude', 'longitude', 'timestamp')
    return JsonResponse(list(gps_data), safe=False)

def map_view(request):
    return render(request, 'map.html')

class GPSDataCreateView(generics.ListCreateAPIView):
    queryset = GPSData.objects.all()
    serializer_class = GPSDataSerializer

class SensorDataList(generics.ListCreateAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer

def vehicle_data_view(request):
    vehicles = VehicleData.objects.all().values('device_id', 'location', 'timestamp')
    return JsonResponse(list(vehicles), safe=False)

@api_view(['GET', 'POST'])
def school_list_create(request):
    if request.method == 'POST':
        serializer = SchoolSerializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    if request.method == 'GET':
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)

class SchoolListCreateView(drf_generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def post(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class VehicleDataListCreateView(generics.ListCreateAPIView):
    queryset = VehicleData.objects.all()
    serializer_class = VehicleDataSerializer

@api_view(['POST'])
def create_vehicle(request):
    data = json.loads(request.body)
    vehicle = VehicleData.objects.create(
        device_id=data['device_id'],
        location=data['location'],
        timestamp=datetime.datetime.utcnow()
    )
    return Response({'id': str(vehicle.id)}, status=201)

@api_view(['GET'])
def read_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(VehicleData, id=vehicle_id)
    return Response({
        'device_id': vehicle.device_id,
        'location': vehicle.location,
        'timestamp': vehicle.timestamp.isoformat()
    })

@api_view(['PUT'])
def update_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(VehicleData, id=vehicle_id)
    data = json.loads(request.body)
    vehicle.device_id = data['device_id']
    vehicle.location = data['location']
    vehicle.timestamp = datetime.datetime.utcnow()
    vehicle.save()
    return Response({'status': 'updated'})

@api_view(['DELETE'])
def delete_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(VehicleData, id=vehicle_id)
    vehicle.delete()
    return Response({'status': 'deleted'})

def school_list_view(request):
    client = MongoClient("mongodb+srv://ivan:,.@cluster0.jksfa.mongodb.net/Iotron?retryWrites=true&w=majority&appName=Cluster0")
    db = client.Iotron
    schools = db.school_list.find()
    return render(request, 'school_list.html', {'schools': schools})
