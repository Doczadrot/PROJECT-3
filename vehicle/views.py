from django_filters.rest_framework import DjangoFilterBackend

from vehicle.models import Car, Moto, Milage
from vehicle.serliazers import CarSerializer, MotoSerializer, MilageSerializer, MotoMilageSerializer, MotoCreateSerialazer
from rest_framework import viewsets, generics

#Cериализаторы
class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    #Дженерики

class MotoCreateAPIViews(generics.CreateAPIView):
    # Здесь нужно использовать сериализатор, предназначенный для создания!
    serializer_class = MotoCreateSerialazer

class MotoListAPIView(generics.ListAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()

class MotoRetriveAPIView(generics.RetrieveAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()

class MotoUpdateAPIView(generics.UpdateAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()

class MotoDestroyAPIView(generics.DestroyAPIView):
    queryset = Moto.objects.all()

class MilageCreateAPIView(generics.CreateAPIView):
    serializer_class = MilageSerializer


class MotoMilageListAPIView(generics.ListAPIView):
    queryset = Milage.objects.filter(moto__isnull=False)
    serializer_class = MotoMilageSerializer

class MilageListAPIView(generics.ListAPIView):
    serializer_class = MilageSerializer
    queryset = Milage.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('car', 'moto')

