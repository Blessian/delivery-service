from rest_framework import serializers

from .models import DeliveryLog


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryLog
        exclude = ['delivery_num']
        read_only_fields = [
            'finish_date', 'pay_state', 'start_date', 'price',
            'buyr_id', 'buyr_name', 'vccode', 'delivery_num', 'delivery_state'
        ]


class DeliveryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryLog
        fields = '__all__'
        read_only_fields = [
            'id', 'start_date', 'quantity', 'price',
            'buyr_id', 'buyr_city', 'buyr_country',
            'buyr_zipx', 'vccode', 'coupon_id', 'finish_date'
        ]


class DeliveryPayStateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryLog
        fields = ['id', 'pay_state']


class DeliveryDeliveryStateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryLog
        fields = ['id', 'delivery_state', 'delivery_num', 'finish_date']
        read_only_fields = ['finish_date']
