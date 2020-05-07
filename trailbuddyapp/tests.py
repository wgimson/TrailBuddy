from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone

# Create your tests here.
class LocationTestCase(TestCase):
    def test_setUp(self):
        self.user1 = User.objects.create_user(username="admin")
        self.assertEqual(self.user1.username, "admin")
