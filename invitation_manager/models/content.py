from django.db import models


class Content(models.Model):
    text = models.TextField()


class ImageFile(models.Model):
    file_name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='content-images')  # optimal size: 1104x621
    order = models.IntegerField(default=0)
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="images")

    class Meta:
        ordering = ['order', 'id']
