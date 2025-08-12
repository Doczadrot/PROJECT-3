from rest_framework import serializers

from vehicle.models import Car, Moto, Milage

class MilageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Milage
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    # Используем SerializerMethodField для вычисляемого поля
    last_milage = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Car
        # Указываем поля, которые нужны
        fields = ("id", "title", "description", "last_milage")

    def get_last_milage(self, instance):
        # Проверяем, что объект существует и у него есть записи о пробеге
        if instance.pk and instance.milage.all().first():
            return instance.milage.all().first().milage
        return 0

class MotoSerializer(serializers.ModelSerializer):
    last_milage = serializers.SerializerMethodField(source='milage_set.all.first.milage') # добавляем запись о последнем пробеге

    class Meta:
        model = Moto
        fields = "__all__"

    def get_last_milage(self, instance):
        # Проверяем, что объект сохранен в БД, прежде чем пытаться получить milage_set
        if instance.pk and instance.milage_set.all().first():
            return instance.milage_set.all().first().milage
        return 0


class MotoMilageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Milage
        fields = ('milage', 'year', 'moto')

class MotoCreateSerialazer(serializers.ModelSerializer):
    milage = MilageSerializer(many=True)

    class Meta:
        model = Moto
        fields = "__all__"

    def create(self, validated_data):

        milage = validated_data.pop('milage')

        moto_item = Moto.objects.create(**validated_data)

        for m in milage:
            Milage.objects.create(**m, moto=moto_item)

        return moto_item

