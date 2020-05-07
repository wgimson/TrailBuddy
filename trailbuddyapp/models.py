from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    note = models.CharField(max_length=500, blank=True)
    lat = models.FloatField(max_length=5)
    lon = models.FloatField(max_length=5)
    create_date = models.DateField(auto_now_add=True)
