from django.db import models

class Image(models.Model):
    text = models.CharField(max_length=100)
    bold = models.CharField(max_length=20)
    image = models.ImageField(upload_to="images/", null=False, blank=False)

    def __str__(self):
        return self.text