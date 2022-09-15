from datetime import date
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from .serializers import \
    DeliverySerializer, \
    DeliveryUpdateSerializer, \
    DeliveryPayStateUpdateSerializer, \
    DeliveryDeliveryStateUpdateSerializer
from .models import DeliveryLog
from coupon.models import Coupon

import pandas as pd

from .utils import validate_date


# Create your views here.
class DeliveryLogViewSet(viewsets.ModelViewSet):
    """

    """
    lookup_field = 'id'

    def get_serializer_class(self):
        """

        :return:
        """
        print('#####', self.action)
        if self.action == 'update':
            return DeliveryUpdateSerializer
        elif self.action == 'update_pay_state':
            return DeliveryPayStateUpdateSerializer
        elif self.action == 'update_delivery_state':
            return DeliveryDeliveryStateUpdateSerializer
        else:
            return DeliverySerializer

    def get_queryset(self):
        """

        :return:
        """
        queryset = DeliveryLog.objects.all()
        search = self.request.GET.get('search', '')

        if validate_date(search):
            queryset = queryset.filter(Q(start_date=search) | Q(finish_date=search))
        elif search:
            queryset = queryset.filter(Q(pay_state=search) | Q(buyr_name=search))
        return queryset

    def get_permissions(self):
        """

        :return:
        """
        if self.action in ('create', 'retrieve', 'update'):
            permission_classes = [IsAuthenticated]
        elif self.action in ('list', 'update-pay-state', 'update-delivery-state'):
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['start_date'] = date.today()
            serializer.validated_data['buyr_id'] = request.user.id
            serializer.validated_data['buyr_name'] = request.user.username

            country_code = serializer.validated_data['buyr_country']
            # 엑셀데이터에서 국가코드를 가져옴
            file = 'data/Country_code.xlsx'
            df_country_code = pd.read_excel(file)
            df_country_code.set_index('country_code', inplace=True)
            vccode = df_country_code.loc[country_code]['country_dcode']
            serializer.validated_data['vccode'] = vccode

            # 제품 가격을 10000원으로 가정
            price = 10000

            # 엑셀데이터에서 배달요금 가져옴
            file = 'data/DeliveryCost.xlsx'
            df_delivery_cost = pd.read_excel(file)
            df_delivery_cost.set_index('quantity', inplace=True)
            country_name = df_country_code.loc[country_code]['country_name']
            delivery_cost = 0
            if country_name != 'South Korea':
                delivery_cost = df_delivery_cost.loc[serializer.validated_data['quantity']][country_name]

            # 쿠폰코드 조회 가격에 적용
            if serializer.validated_data['coupon_id']:
                coupon = Coupon.objects.get(id=serializer.validated_data['coupon_id'])

                if coupon.discount_target == 'PRODUCT' and coupon.discount_type is 'PERCENTAGE':
                    price = price * (100 - int(coupon.discount_amount)) / 100
                if coupon.discount_target == 'PRODUCT' and coupon.discount_type is 'FLAT':
                    price = price - int(coupon.discount_amount)
                if coupon.discount_target == 'DELIVERY_COST' and coupon.discount_type is 'PERCENTAGE':
                    delivery_cost = delivery_cost * (100 - int(coupon.discount_amount)) / 100
                if coupon.discount_target == 'DELIVERY_COST' and coupon.discount_type is 'FLAT':
                    delivery_cost = delivery_cost - int(coupon.discount_amount)

            serializer.validated_data['price'] = serializer.validated_data['quantity'] * price + delivery_cost
            # 한국이 아니면 달러로 표시(환율 1200원으로 가정)
            if country_code is not 'KR':
                serializer.validated_data['price'] = serializer.validated_data['price'] / 1200

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=['put', 'patch'], name='Update pay_state')
    def update_pay_state(self, request, **kwargs):
        instance = self.get_object()
        serializer = DeliveryPayStateUpdateSerializer(
            data={'id': kwargs['id'], 'pay_state': request.data['pay_state']}
        )
        if serializer.is_valid(raise_exception=True):
            instance.pay_state = serializer.validated_data['pay_state']
            self.perform_update(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put', 'patch'], name='Update delivery_state')
    def update_delivery_state(self, request, **kwargs):
        instance = self.get_object()
        serializer = DeliveryDeliveryStateUpdateSerializer(
            data={'id': kwargs['id'], 'delivery_state': request.data['delivery_state']}
        )

        if serializer.is_valid(raise_exception=True):
            instance.delivery_state = serializer.validated_data['delivery_state']
            print('#####', serializer.validated_data['delivery_state'] == '배송완료')

            if serializer.validated_data['delivery_state'] == '배송완료':
                instance.finish_date = date.today()
                serializer.validated_data['finish_date'] = date.today()

            self.perform_update(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
