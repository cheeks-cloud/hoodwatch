from django.db import models
from django.contrib.auth.models import User
from neighborhood.models import Neighborhood

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='hood_profile_images/', blank=True, null=True)
    hood = models.ForeignKey(Neighborhood, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username.title()}'s Profile "

    def create_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    
    def update_profile(self, user, image, hood):
        self.user = user
        self.image = image
        self.hood = hood
        self.save()

        
