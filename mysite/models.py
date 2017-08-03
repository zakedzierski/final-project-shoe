from django.db import models

class Shoes(models.Model):
    name = models.CharField(max_length=30)
    brand_choices = (
        (ADDIDAS, 'Addidas'),
        (NIKE, 'Nike'),
        (NEW BALANCE, 'New Balnce'),)
    brand = models.CharField(max_length=1,
                                      choices=brand_choices
                                      default=ADDIDAS)
    miles_run = models.IntegerField(default=0)
