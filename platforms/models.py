from django.db import models


# Create your models here.
class Platform(models.Model):
    url = models.URLField()
    name = models.TextField()
    phone = models.TextField()
    email = models.TextField()
    connection_date = models.DateTimeField()
