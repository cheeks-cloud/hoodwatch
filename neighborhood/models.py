from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)
    occupants = models.PositiveIntegerField(default=0, blank=True)
    admin = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, default=None)

    def __str__(self):
        return self.name.title()


class Business(models.Model):
    name = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    email = models.EmailField(max_length=1000)

    def __str__(self):
        return self.name.title()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=1000, null=True)
    content = models.TextField()
    hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title.title()