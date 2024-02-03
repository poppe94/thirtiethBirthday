from django.db import models


class Content(models.Model):
    text = models.TextField()


class ImageFile(models.Model):
    file_name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='content-images')
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="images")
