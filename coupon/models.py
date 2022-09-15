from django.db import models


# Create your models here.
class Coupon(models.Model):
    coupon_code = models.CharField(max_length=30, blank=False, null=False, unique=True)
    title = models.CharField(max_length=30, blank=False, null=False)

    DISCOUNT_TYPE_CHOICE = [
        ('FLAT', 'FLAT'),
        ('PERCENTAGE', 'PERCENTAGE')
    ]
    discount_type = models.CharField(max_length=10, choices=DISCOUNT_TYPE_CHOICE, blank=False, null=False)

    DISCOUNT_TARGET_CHOICE = [
        ('PRODUCT', 'PRODUCT'),
        ('DELIVERY_COST', 'DELIVERY_COST'),
    ]
    discount_target = models.CharField(max_length=13, choices=DISCOUNT_TARGET_CHOICE, blank=False, null=False)

    discount_amount = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)


class CouponLog(models.Model):
    coupon_id = models.PositiveIntegerField(blank=False, null=False)
    user_id = models.PositiveIntegerField(blank=False, null=False)
    discounted_price = models.DecimalField(blank=False, null=False)
    used_date = models.DateField(blank=False, null=False)
