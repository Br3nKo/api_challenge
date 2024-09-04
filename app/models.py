from django.db import models
from datetime import datetime

class Country(models.Model):
    name = models.CharField(max_length=255)
    countryCode = models.CharField(max_length=10)
    createdAt = models.DateTimeField()
    groupId = models.IntegerField()

    def __str__(self):
        return self.name
