from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)
    occupants = models.IntegerField(default=0, blank=True)
    admin = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, default=None)

    