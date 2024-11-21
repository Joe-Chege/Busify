from django.urls import path
from .views import (
    GPSDataCreateView, 
    map_view, 
    SensorDataList, 
    SchoolListCreateView, 
    VehicleDataListCreateView, 
    vehicle_data_view,
    create_vehicle,
    read_vehicle,
    update_vehicle,
    delete_vehicle
)

urlpatterns = [
    path('gps-data/', GPSDataCreateView.as_view(), name='gps_data_create'),
    path('map/', map_view, name='map_view'),
    path('sensor-data/', SensorDataList.as_view(), name='sensor_data_list'),
    path('schools/', SchoolListCreateView.as_view(), name='school_list_create'),
    path('vehicle-data/', VehicleDataListCreateView.as_view(), name='vehicle_data_list_create'),
    path('vehicles/', create_vehicle, name='create_vehicle'),
    path('vehicles/<str:vehicle_id>/', read_vehicle, name='read_vehicle'),
    path('vehicles/<str:vehicle_id>/update/', update_vehicle, name='update_vehicle'),
    path('vehicles/<str:vehicle_id>/delete/', delete_vehicle, name='delete_vehicle'),
    path('vehicle-data/', vehicle_data_view, name='vehicle_data'),
]
