from cgi import test
from urllib import response
from django.shortcuts import redirect
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import models
from . import views

# Create your tests here.

class LoginTest(TestCase):

    def setUp(self):
        users = models.User
        user1 = users.objects.create_user(username='nice', password='420')
        user2 = users.objects.create_user(username='cool', password='69')

    def test_is_page_exist(self):
        c =Client()
        response = c.get(reverse('login_page:login'))
        self.assertEqual(response.status_code, 200)


    def test_is_authenticated(self):
        c = Client()
        c.login(username='nice', password='420')
        response = c.get(reverse('login_page:login'))
        self.assertEqual(response.context['user'].is_authenticated, True)


