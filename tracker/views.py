from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_mongoengine import generics
from .models import GPSData, SensorData, VehicleData, School
from .serializers import GPSDataSerializer, SensorDataSerializer, SchoolSerializer, VehicleDataSerializer
import json
import datetime

def gps_data_view(request):
    gps_data = GPSData.objects.all().values('device_id', 'latitude', 'longitude', 'timestamp')
    return JsonResponse(list(gps_data), safe=False)

def map_view(request):
    return render(request, 'map.html', {})

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
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            school = serializer.save()
            return Response(SchoolSerializer(school).data, status=201)
        return Response(serializer.errors, status=400)
    
    if request.method == 'GET':
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)

class SchoolListCreateView(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

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
