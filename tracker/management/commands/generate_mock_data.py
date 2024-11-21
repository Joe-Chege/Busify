from django.core.management.base import BaseCommand
from tracker.models import VehicleData, School
import random
import datetime

class Command(BaseCommand):
    help = 'Generate mock vehicle data'

    def handle(self, *args, **kwargs):
        schools = list(School.objects.all())
        for _ in range(10):  # Generate 10 vehicles
            school = random.choice(schools)
            VehicleData.objects.create(
                device_id=f"vehicle_{random.randint(1, 1000)}",
                location=[school.location['coordinates'][0], school.location['coordinates'][1]],
                timestamp=datetime.datetime.utcnow()
            )
        self.stdout.write(self.style.SUCCESS('Successfully generated mock data'))
