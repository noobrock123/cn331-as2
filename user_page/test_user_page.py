from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import models
from django.shortcuts import redirect
from .models import Subject
from . import views

# Create your tests here.

class user_functions_test(TestCase):

	def setUp(self):
		Subject.objects.create(subject_id="TS1", name="test_subject1", \
                n_seats=100, is_requestable=True)
		Subject.objects.create(subject_id="TS2", name="test_subject2", \
                n_seats=1, is_requestable=True)
		Subject.objects.create(subject_id="TS3", name="test_subject3", \
                n_seats=100)
		Subject.objects.create(subject_id="TS4", name="test_subject4", \
				n_seats=50)

		users = models.User
		user1 = users.objects.create_user(username='nice', password='420')
		user2 = users.objects.create_user(username='cool', password='69')

		Subject.objects.get(pk="TS1").students.add(user1)
		Subject.objects.get(pk="TS1").students.add(user2)
		Subject.objects.get(pk="TS2").students.add(user2)

	#==========Check for HTML page's integrity==========
	def test_is_page_exist(self):
		c = Client()
		c.login(username='cool', password='69')
		response = c.get(reverse('user_page:front_page'))
		self.assertEqual(response.status_code, 200)

		response = c.get(reverse('user_page:quota_request_page'))
		self.assertEqual(response.status_code, 200)

		response = c.get(reverse('user_page:show_quota_result'))
		self.assertEqual(response.status_code, 200)
	
	#==========Check models' functions==========
	def test_is_subject_found(self):
		self.assertEqual(len(Subject.get_subject("TS4", 2022)), 1)
		self.assertEqual(len(Subject.get_subject("TS5", 2022)), 0)
	
	#==========Check if functions used for request_page are working properly==========
	def test_is_user_authenticated(self):
		c = Clinet()
		response = c.get(reverse('user_page:front_page'))

		#User input url path
		self.assertEqual(response.status_code, 302)

	def test_is_subject_found(self):
		import datetime
		self.assertEqual(len(Subject.get_subject("TS4", 2022)), 1)
	
	def test_acquiring_subjects(self):
		c = Client()
		#Login first
		c.login(username='cool', password='69')
		c.get(reverse('user_page:quota_request_page'))
		
		#User selecting TS1
		c.get(reverse('user_page:acquire_quota', kwargs={'sub_id':'TS1'}))
		self.assertEqual(c.session['already_acquired'], True)

		c.get(reverse('user_page:quota_request_page'))
		
		#User acquiring subject 
		c.get(reverse('user_page:acquire_quota', kwargs={'sub_id':'TS4'}))
		self.assertEqual(c.session['already_acquired'], False)

		#User removing selected subject
		temp = c.session['selected_subjects']
		c.get(reverse('user_page:remove_quota', kwargs={'sub_id':'TS4'}))
		self.assertEqual(c.session['selected_subjects'] == temp, False)
	
	def test_accepting_subjects(self):
		c = Client()
		c.login(username='cool', password='69')
		c.get(reverse('user_page:quota_request_page'))
		c.get(reverse('user_page:acquire_quota', kwargs={'sub_id':'TS4'}))
		c.post(reverse('user_page:accept_quota'))	
		found_subject = [models.User.objects.get(username='cool').subjects.get(pk='TS4')]
		self.assertEqual(len(found_subject), 1)

	def test_removing_acquired_subjects(self):
		c = Client()
		c.login(username='cool', password='69')

		#User removing subject 'TS2'
		response = c.post(reverse('user_page:remove_acquired_quota', kwargs={'sub_id':'TS2'}))
		self.assertEqual(response.status_code, 302)
	
	def test_user_logout(self):
		c = Client()
		c.login(username='cool', password='69')

		#User loging out
		response = c.post(reverse('user_page:log_out'))
		self.assertEqual(response.status_code, 302)

	def test_is_subject_full(self):
		self.assertEqual(len(Subject.objects.get(pk="TS2").students.all()), Subject.objects.get(pk="TS2").n_seats)
	

	