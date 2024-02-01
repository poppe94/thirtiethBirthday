import random
import string

from django.contrib.auth import get_user_model
from django.db import models

from . import constants

User = get_user_model()
# Create your models here.


class GuestInfo(models.Model):
    overnight_stay = models.BooleanField(default=False)
    food_preferences = models.CharField(
        choices=constants.FOOD_PREFERENCES_CHOICES,
        default=constants.FOOD_PREFERENCES_CHOICES[0],
        max_length=64,
        blank=True
    )

    class Meta:
        abstract = True


class Guest(GuestInfo):
    display_name = models.CharField(max_length=128, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    link_identifier = models.CharField(max_length=128, unique=True, blank=True, editable=False)

    visited = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Gast"
        verbose_name_plural = "Gäste"

    def _set_link_identifier(self):
        while not self.link_identifier:
            new_identifier = ''.join(random.sample(string.hexdigits, constants.LINK_IDENTIFIER_LENGTH))

            if not Guest.objects.filter(link_identifier__exact=new_identifier).exists():
                self.link_identifier = new_identifier

    def save(self, *args, **kwargs):
        self._set_link_identifier()
        super().save(*args, **kwargs)


class Entourage(GuestInfo):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Begleitung"
        verbose_name_plural = "Begleitung"
