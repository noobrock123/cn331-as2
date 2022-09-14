from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import path, include
from .models import Subject
from django import forms
from django.contrib.auth import logout, models

# Create your views here.

users = models.User
def front_page(request):
	print(request.user.is_authenticated)
	if not request.user.is_authenticated:
		return redirect('login_page:login')
	from django.utils import timezone
	hour = timezone.localtime().hour
	minute = timezone.localtime().minute
	time_format = ""
	if hour >= 0 and hour < 11:
		if hour == 0:
			hour = 12
		time_format = "AM"
	elif hour > 12 and hour <= 23:
		hour = hour % 12
		time_format = "PM"
	else:
		time_format = "PM"
	if minute < 10:
		time_format = str(hour) + ":0" + str(minute) + time_format
	else:
		time_format = str(hour) + ":" + str(minute) + time_format
	name = request.user.first_name 
	print(request.user.username)
	print(request.user.students.all())
	#print(request.user.students)
	return render(request, 'user_page/user_page.html', {
	'name': name,
	'time': time_format})
	
class Search_subjects(forms.Form):
	search = forms.CharField(label="ค้นหารายวิชา (รหัสวิชา):", min_length=2)

def quota_page(request):
	n_students = []
	context = {}
	if (request.method == 'POST'):
		sub_id = request.POST['subject_id']	
		if len(sub_id) <= 1:
			search_result = []
			return render(request, 'user_page/request_page.html',
			{'message': "ไม่พบวิชาที่ค้นหา"})
		else:
			search_result = Subject.get_subject(sub_id)
			return render(request, 'user_page/request_page.html', 
			{'searched_subjects': search_result,
			})
	return render(request, 'user_page/request_page.html')

def acquire_quota(request, sub_id):
	print(sub_id)
	return render(request, 'user_page/request_page.html')

def quota_result(request):
	return render(request, 'user_page/request_result.html')

def log_out(request):
	logout(request)
	return redirect('login_page:login')


