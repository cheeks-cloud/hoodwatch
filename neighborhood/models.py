from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    hood_name = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)
    occupants = models.PositiveIntegerField(default=1, blank=True)
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, default=None, null=True)

    def __str__(self):
        return self.hood_name.title()

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    def update_neigborhood(self, name, location, occupants, admin):
        self.name = name
        self.location = location
        self.occupants = occupants
        self.admin = admin
        self.save()

    @staticmethod
    def find_neighborhood_by_id(id):
        hood = Neighborhood.objects.get(id=id)
        return hood
    
    @staticmethod
    def update_occupants(hood):
        hood.occupants += 1
        hood.save()
        



class Business(models.Model):
    business_name = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=1000)

    def __str__(self):
        return self.business_name.title()
    
    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def update_business(self, name, user, hood, email):
        self.name = name
        self.user = user
        self.hood = hood 
        self.email = email
        self.save()

    @staticmethod
    def find_business_by_id( id):
        business = Business.objects.get(id=id)
        return business
    


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=1000, null=True)
    image = models.ImageField(upload_to='hood_posts/', blank=True, null=True)
    content = models.TextField()
    hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title.title()

    def create_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def update_post(self, user, title, image, content, hood):
        self.user = user
        self.title = title
        self.image = image
        self.content = content
        self.hood = hood
        self.save()
