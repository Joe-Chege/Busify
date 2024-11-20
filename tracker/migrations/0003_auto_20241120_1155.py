# Generated by Django 3.1.12 on 2024-11-20 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_sensordata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gpsdata',
            name='location',
        ),
        migrations.AddField(
            model_name='gpsdata',
            name='latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='gpsdata',
            name='longitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='gpsdata',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='shapefiledata',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
