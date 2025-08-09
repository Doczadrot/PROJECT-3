from rest_framework import serializers

from vehicle.models import Car, Moto, Milage


class CarSerializers(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = "__all__"

class MotoSerializers(serializers.ModelSerializer):

    class Meta:
        model = Moto
        fields = "__all__"

class MilageSerializers(serializers.ModelSerializer):

    class Meta:
        model = Milage
        fields = "__all__"

