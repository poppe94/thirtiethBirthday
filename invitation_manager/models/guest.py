import random
import string

from django.contrib.auth.models import User
from django.db import models

from invitation_manager import constants

# Create your models here.


class GuestInfo(models.Model):
    display_name = models.CharField(max_length=128, blank=True)
    overnight_stay = models.BooleanField(default=False)
    food_preferences = models.CharField(
        choices=constants.FOOD_PREFERENCES_CHOICES,
        default=constants.FOOD_PREFERENCES_CHOICES[0][0],
        max_length=64,
    )

    class Meta:
        abstract = True


class Guest(GuestInfo):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    link_identifier = models.CharField(max_length=128, unique=True, blank=True, editable=False)
    note = models.TextField(blank=True)
    # true when info-form was filled, naming is meh
    visited_on = models.DateTimeField(blank=True, null=True)
    confirmed = models.BooleanField(default=False)
    confirmed_on = models.DateTimeField(blank=True, null=True)

    cancelled_on = models.DateTimeField(blank=True, null=True)
    cancelled = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Gast"
        verbose_name_plural = "Gäste"

    def __str__(self):
        if self.display_name:
            if self.display_name != self.user.username:
                return f"{self.display_name} ({self.user.username})"
            else:
                return self.display_name

        return self.user.username

    def _set_link_identifier(self):
        while not self.link_identifier:
            new_identifier = ''.join(random.sample(string.hexdigits, constants.LINK_IDENTIFIER_LENGTH))

            if not Guest.objects.filter(link_identifier__exact=new_identifier).exists():
                self.link_identifier = new_identifier

    def save(self, *args, **kwargs):
        self._set_link_identifier()
        super().save(*args, **kwargs)

    def reset(self):
        self.entourage_set.all().delete()
        self.overnight_stay = False
        self.food_preferences = constants.FOOD_PREFERENCES_CHOICES[0][0]
        self.confirmed = False
        self.save()

    def wants_overnight_stay(self):
        return self.entourage_set.filter(overnight_stay=True).exists() or self.overnight_stay


class Entourage(GuestInfo):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Begleitung"
        verbose_name_plural = "Begleitung"
