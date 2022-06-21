from django.test import TestCase
from django.contrib.auth.models import User
from users.models import *
from neighborhood.models import *

# Create your tests here.
class NeigborhoodTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='samuel', email='samuel.martins3.sm@gmail.com', password='thesmartcoder')
        self.hood = Neighborhood.objects.create(admin=self.user, hood_name='my hood', location='beijing road')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.hood, Neighborhood))

    def test_save(self): 
        self.user.save()
        all_hoods = Neighborhood.objects.all()
        self.assertEquals(len(all_hoods),1)

    def test_update(self):
        self.user.save()
        self.hood.user = self.user
        self.hood.hood_name = 'my new name'
        self.hood.location = 'beijing road'
        self.hood.save()
        self.assertEquals(self.hood.hood_name, 'my new name')

    def test_delete(self):
        self.user.save()
        self.new_hood = Neighborhood.objects.create(admin=self.user, hood_name='my hood 1', location='katani road')
        self.new_hood.save()
        self.new_hood.delete()
        all_hoods = Neighborhood.objects.all()
        self.assertEquals(len(all_hoods),1)

    def test_update_occupants(self):
        self.user.save()
        self.hood.save()
        self.new_user = User.objects.create(username='jim', email='samuel.martins3.sm@gmail.com', password='thesmartcoder')
        self.user.profile.hood = self.hood
        self.hood.occupants += 1
        self.assertEquals(self.hood.occupants, 2)

    def test_find_hood_by_id(self):
        self.user.save()
        self.hood.save()
        found = Neighborhood.find_neighborhood_by_id(self.hood.id)
        self.assertEquals(self.hood, found)



class BusinessTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='samuel', email='samuel.martins3.sm@gmail.com', password='thesmartcoder')
        self.hood = Neighborhood.objects.create(admin=self.user, hood_name='my hood', location='beijing road')
        self.business = Business.objects.create(business_name='new business', user=self.user, hood=self.hood, email='business@gmail.com')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    def test_save(self): 
        self.business.save()
        all_businesses = Business.objects.all()
        self.assertEquals(len(all_businesses),1)

    def test_update(self):
        self.business.business_name = 'my new name'
        self.business.save()
        self.assertEquals(self.business.business_name, 'my new name')

    def test_delete(self):
        self.business.delete()
        all_businesses = Business.objects.all()
        self.assertEquals(len(all_businesses), 0)

    def test_find_business_by_id(self):
        self.business = Business.objects.create(business_name='new business', user=self.user, hood=self.hood, email='business@gmail.com')
        self.business.save()
        found = Business.find_business_by_id(self.business.id)
        self.assertEquals(self.business, found)



class PostTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='samuel', email='samuel.martins3.sm@gmail.com', password='thesmartcoder')
        self.hood = Neighborhood.objects.create(admin=self.user, hood_name='my hood', location='beijing road')
        self.post = Post.objects.create(title='title', user=self.user, hood=self.hood, content='my content')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save(self): 
        self.post.save()
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts),1)

    def test_update(self):
        self.post.title = 'updated title'
        self.post.save()
        self.assertEquals(self.post.title, 'updated title')

    def test_delete(self):
        self.post.delete()
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 0)
