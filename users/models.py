from django.db import models
from django.contrib.auth.models import User
from neighborhood.models import Neighborhood

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='hood-default.png', upload_to='hood_profile_images/')
    hood = models.ForeignKey(Neighborhood, on_delete=models.DO_NOTHING)
