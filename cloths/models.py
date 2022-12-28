import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.


class Cloth(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    style = models.CharField(max_length=200)
    stylist = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)
    # cover = models.FileField(upload_to='covers/')

    def __str__(self):
        return self.style

    def get_absolute_url(self):
        # return reverse('cloth_detail', args=[str(self.pk)])
        return reverse('cloth_detail', kwargs={'pk': str(self.pk)})


class Review(models.Model):
    cloth = models.ForeignKey(
        Cloth,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    review = models.CharField(max_length=255)
    stylist = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review
