from rest_framework import serializers

from .models import DeliveryLog


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryLog
        fields = '__all__'


class DeliveryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryLog
        fields = '__all__'
        read_only_fields = '__all__'


class DeliveryPayStateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryLog
        fields = ['id', 'pay_state']


class DeliveryDeliveryStateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryLog
        fields = ['id', 'delivery_state']
