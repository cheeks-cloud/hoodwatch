from django.test import TestCase
from django.contrib.auth.models import User
from users.models import *


# Create your tests here.
class UserTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create( username='samuel', email='samuel.martins3.sm@gmail.com', password='thesmartcoder' )
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_user,User))

    def test_save(self):
        self.new_user.save()
        all_users = User.objects.all()
        self.assertEquals(len(all_users),1)

    def test_update_user(self):
        self.new_user.save()
        self.new_user.username = 'charles'
        self.new_user.email = 'charles@gmail.com'
        self.new_user.password = 'testuserokunzo'
        self.new_user.save()
        self.assertEqual(self.new_user.username, 'charles')

    def test_delete(self):
        self.new_user.save()
        test_user = User(username = 'simple_user',password='testuser123',email='testuser@domain.com')
        test_user.save()
        self.new_user.delete()
        all_users = User.objects.all()
        self.assertEquals(len(all_users),1)


class ProfileTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create( username='samuel', email='samuel.martins3.sm@gmail.com', password='thesmartcoder' )
        self.new_user.save()
        self.new_profile = Profile.objects.filter(user=self.new_user).first()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_profile(self):
        self.another_user = User.objects.create( username='tom', email='tom.sm@gmail.com', password='thesmartcoder' )
        self.another_user.save()
        self.another_profile = Profile.objects.filter(user=self.new_user).first()
        all_profiles = Profile.objects.all()
        self.assertEquals(len(all_profiles),2)

    def test_update_profile(self):
        self.new_profile.work_title = 'backend engineer'
        self.new_profile.bio = 'this is me'
        self.new_profile.save()
        self.assertEquals(self.new_profile.bio, 'this is me')

    def test_delete_profile(self):
        self.dean_user = User.objects.create(username='dean', password='deantheman', email='dean@domain.com')
        self.dean_user.save()
        self.dean_profile = Profile.objects.filter(user=self.dean_user).first()
        self.dean_user.delete()
        all_profiles = Profile.objects.all()
        self.assertEquals(len(all_profiles),1)