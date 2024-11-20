import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GeoTracker.settings')
django.setup()

from tracker.models import School

# Your test code here
school = School(name="Test School", location=[-1.2921, 36.8219], address="Test Address")
school.save()

print(School.objects.all())
