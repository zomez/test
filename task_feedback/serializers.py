from rest_framework import serializers

from users_customs.models import CustomUser
from .models import DepPay, RayPay, StatusTask


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusTask
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'email',
            'id'
        ]


class RayPaySerializer(serializers.ModelSerializer):
    class Meta:
        model = RayPay
        fields = '__all__'

    def create(self, validated_data):
        return RayPay(**validated_data)


class DepPaySerializer(serializers.ModelSerializer):

    class Meta:
        model = DepPay
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        return DepPay.objects.create(**validated_data)




