from django.db import models

# Create your models here.

BRAND_CHOICES = (
    ('addidas','Addidas'),
    ('nike', 'Nike'),
    ('new balance','New Balance'),
    ('Asics','Asics'),
    ('Brooks','Brooks'),
    ('Under Armour','Under Armour'),
)

ICON_CHOICES = (
                ('running_shoe.png', 'Running Shoe'),
                ('running_spike.png', 'Running Spike'),
                ('competition_running_shoe.png', 'Competition Running Shoe'),
        )

class MyShoe(models.Model):
    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=30, choices=BRAND_CHOICES, default='addidas')
    icon= models.CharField(max_length=30, choices=ICON_CHOICES, default='running_shoe.png')
    miles_run = models.IntegerField(default=0)
