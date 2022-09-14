from django.db import models
from django.utils.translation import gettext_lazy as _

import pandas as pd


class DeliveryLog(models.Model):
    start_date = models.DateField()
    finish_date = models.DateField()

    PAY_STATE_CHOICE = [
        ('결재완료', '결재완료'),
        ('결재취소', '결재취소')
    ]
    pay_state = models.CharField(max_length=10, choices=PAY_STATE_CHOICE, default='결재완료')

    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    buyr_city = models.CharField(max_length=50, blank=False, null=False)

    # data디렉토리의 엑셀파일에서 국가이름 정보를 가져옴
    file = '../data/Country_code.xlsx'
    df_excel = pd.read_excel(file, header=0)
    BUYR_COUNTRY_CHOICE = [(row.country_name, row.contry_code) for row in df_excel.iterrows()]
    buyr_country = models.CharField(max_length=2, choices=BUYR_COUNTRY_CHOICE, blank=False, null=False)

    buyr_zipx = models.CharField(max_length=10, blank=False, null=False)
    vccode = models.PositiveIntegerField()
    delivery_num = models.CharField(max_length=50)
    
    DELIVERY_STATE = [
        ('배송준비', '배송준비'),
        ('배송중', '배송중'),
        ('배송완료', '배송완료')
    ]
    delivery_state = models.CharField(max_length=10, choices=DELIVERY_STATE, default='배송준비')

    coupon_code = models.CharField(max_length=50)
    discounted = models.PositiveIntegerField()