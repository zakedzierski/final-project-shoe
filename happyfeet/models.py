from django.db import models
from django.contrib.auth.models import User

# Create your models here.

BRAND_CHOICES = (
    ('Addidas','Addidas'),
    ('Nike', 'Nike'),
    ('New Balance','New Balance'),
    ('Asics','Asics'),
    ('Brooks','Brooks'),
    ('Under Armour','Under Armour'),
)

ICON_CHOICES = (
                ('Running Shoe', 'Running Shoe'),
                ('Running Spike', 'Running Spike'),
                ('Competition Running Shoe', 'Competition Running Shoe'),
        )

class MyShoe(models.Model):
    user = models.ForeignKey(User, null=True)
    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=30, choices=BRAND_CHOICES, default='addidas')
    icon= models.CharField(max_length=30, choices=ICON_CHOICES, default='running_shoe.png')
    miles_run = models.IntegerField(default=0)

    # def __str__(self):
    #     return " ".join([str(self.user), str(self.name), str(self.brand), str(self.icon), str(self.miles_run)])
