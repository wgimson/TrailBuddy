from .models import Location
from rest_framework import viewsets, permissions
from .serializers import LocationSerializer

#Location Viewsets
class LocationViewset(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LocationSerializer