"""Deck's Models."""
from django.db import models


class Card(models.Model):

    image = models.ImageField(
        'imagen',
        upload_to='images',
    )
    number = models.IntegerField(
        'numero',
    )
    name = models.CharField(
        'nombre',
        max_length=50,
    )
    cross_image = models.ImageField(
        'imagen',
        upload_to='cross_images',
        null=True,
    )

    class Meta:
        verbose_name = "Carta"
        verbose_name_plural = "Cartas"

    def __str__(self):
        return self.name
