from django.db import models
from django.urls import reverse

# Create your models here.


class Cloth(models.Model):
    style = models.CharField(max_length=200)
    stylist = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.style

    def get_absolute_url(self):
        return reverse('cloth_detail', args=[str(self.pk)])
