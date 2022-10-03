from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import models
from .models import Subject

# Create your tests here.

class user_functions_test(TestCase):

    __users = models.User
    def set_up(self):
        sub1 = Subject.objects.create(subject_id="TS1", subject_name="test_subject1", \
                n_seat=100, is_requestable=True)
        sub2 = Subject.objects.create(subject_id="TS2", subject_name="test_subject2", \
                n_seat=1, is_requestable=True)
        sub3 = Subject.objects.create(subject_id="TS3", subject_name="test_subject3", \
                n_seat=100)
        
        user1 = users.objects.create(username="nice", password="420")
        user2 = users.objects.create(username="cool", password="69")



