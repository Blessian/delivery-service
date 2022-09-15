from django.db import models


# Create your models here.
class Coupon(models.Model):
    coupon_code = models.CharField(max_length=30, unique=True)
    title = models.CharField(max_length=30)

    DISCOUNT_TYPE_CHOICE = [
        ('FLAT', 'FLAT'),
        ('PERCENTAGE', 'PERCENTAGE')
    ]
    discount_type = models.CharField(max_length=10, choices=DISCOUNT_TYPE_CHOICE)

    DISCOUNT_TARGET_CHOICE = [
        ('PRODUCT', 'PRODUCT'),
        ('DELIVERY_COST', 'DELIVERY_COST'),
    ]
    discount_target = models.CharField(max_length=13, choices=DISCOUNT_TARGET_CHOICE)

    discount_amount = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)


class CouponLog(models.Model):
    coupon_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    used_date = models.DateField()
