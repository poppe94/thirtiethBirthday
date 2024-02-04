from django.db import models


class ImageFile(models.Model):
    file_name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='content-images')  # optimal size: 1104x621
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.file_name + f' ({self.order})'


class Location(models.Model):
    image = models.ForeignKey(ImageFile, on_delete=models.PROTECT, null=True, blank=True)
    address = models.CharField(max_length=64)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, default=0.0)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, default=0.0)
    text = models.TextField(blank=True)
    arrival_description = models.TextField(blank=True)

    def get_google_maps_link(self):
        return f'https://www.google.com/maps?saddr=My+Location&daddr={self.latitude},{self.longitude}'


class Event(models.Model):
    date = models.DateField()
    time = models.TimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)


class Content(models.Model):
    intro_text = models.TextField(blank=True)
    subheader = models.TextField(blank=True)
    images = models.ManyToManyField(ImageFile, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
