from .models import GPSData, SensorData, VehicleData, School
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework_mongoengine import generics
from rest_framework_mongoengine.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GPSDataSerializer, SensorDataSerializer, SchoolSerializer, VehicleDataSerializer

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
    vehicle_data = VehicleData.objects.all()
    return render(request, 'vehicle_data.html', {'vehicle_data': vehicle_data})

@api_view(['GET', 'POST'])
def school_list_create(request):
    if request.method == 'POST':
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            school = serializer.save()  # Save school to the database
            return Response(SchoolSerializer(school).data, status=201)
        return Response(serializer.errors, status=400)
    
    if request.method == 'GET':
        schools = School.objects()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)

class SchoolListCreateView(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class VehicleDataListCreateView(generics.ListCreateAPIView):
    queryset = VehicleData.objects.all()
    serializer_class = VehicleDataSerializer
