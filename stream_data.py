import time
import random
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from tracker.models import VehicleData, School
import datetime

def stream_vehicle_data():
    channel_layer = get_channel_layer()
    vehicles = VehicleData.objects.all()
    schools = list(School.objects.all())

    while True:
        for vehicle in vehicles:
            new_school = random.choice(schools)
            vehicle.location = [new_school.location['coordinates'][0], new_school.location['coordinates'][1]]
            vehicle.timestamp = datetime.datetime.utcnow()
            vehicle.save()

            async_to_sync(channel_layer.group_send)(
                "vehicles",
                {
                    "type": "vehicle.update",
                    "message": {
                        "device_id": vehicle.device_id,
                        "location": vehicle.location,
                        "timestamp": vehicle.timestamp.isoformat()
                    }
                }
            )
            time.sleep(1)

if __name__ == "__main__":
    stream_vehicle_data()
