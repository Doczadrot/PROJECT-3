from vehicle.models import Car, Moto, Milage
from vehicle.serliazers import CarSerializers, MotoSerializers, MilageSerializers, MotoMilageSerializer
from rest_framework import viewsets, generics

#Cериалиторы
class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializers
    queryset = Car.objects.all()

    #Дженерики

class MotoCreateAPIViews(generics.CreateAPIView):
    serializer_class = MotoSerializers

class MotoListAPIView(generics.ListAPIView):
    serializer_class = MotoSerializers
    queryset = Moto.objects.all()

class MotoRetriveAPIView(generics.RetrieveAPIView):
    serializer_class = MotoSerializers
    queryset = Moto.objects.all()

class MotoUpdateAPIView(generics.UpdateAPIView):
    serializer_class = MotoSerializers
    queryset = Moto.objects.all()

class MotoDestroyAPIView(generics.DestroyAPIView):
    queryset = Moto.objects.all()

class MilageCreateAPIView(generics.CreateAPIView):
    serializer_class = MilageSerializers


class MotoMilageListAPIView(generics.ListAPIView):
    queryset = Milage.objects.filter(moto__isnull=False)
    serializer_class = MotoMilageSerializer

