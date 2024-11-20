from django.urls import path
from .views import GPSDataCreateView, map_view, SensorDataList, SchoolListCreateView, VehicleDataListCreateView

urlpatterns = [
    path('gps-data/', GPSDataCreateView.as_view(), name='gps_data_create'),
    path('map/', map_view, name='map_view'),
    path('sensor-data/', SensorDataList.as_view(), name='sensor_data_list'),
    path('schools/', SchoolListCreateView.as_view(), name='school_list_create'),
    path('vehicle-data/', VehicleDataListCreateView.as_view(), name='vehicle_data_list_create'),
]