from django.db import models


class Chicken(models.Model):
    COOL = 'CO'
    MEDIUM = 'ME'
    HOT = 'HO'

    SPICY_VALUES = (
        (COOL, 'Cool'),
        (MEDIUM, 'Medium'),
        (HOT, 'Hot'),
    )

    spiciness = models.CharField(max_length=2, choices=SPICY_VALUES)
    name = models.CharField(max_length=255)
