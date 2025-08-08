from vehicle.models import Car
from vehicle.serliazers import CarSerializers
from rest_framework import viewsets


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializers
    queryset = Car.objects.all()