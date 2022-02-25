from django.test import TestCase, Client
from django.urls import resolve, reverse
from accounts.models import User

class TestUrl(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username = 'admin',
            description = 'hi',
            password = 'ad312min',
        )

    def test_index_url(self):
        u = User.objects.get(username='admin')
        assert u.description == 'hi'
        