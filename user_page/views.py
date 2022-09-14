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
	#print(request.user.students)
	return render(request, 'user_page/user_page.html', {
	'name': name,
	'time': time_format})
	
class Search_subjects(forms.Form):
	search = forms.CharField(label="ค้นหารายวิชา (รหัสวิชา):", min_length=2)

search_result = []
def quota_page(request):
	if 'selected_subjects' not in request.session:
		request.session['selected_subjects'] = []
	n_students = []
	context = {}
	if (request.method == 'POST'):
		sub_id = request.POST['subject_id']	
		search_result = Subject.get_subject(sub_id)
		if len(search_result) == 0 or len(sub_id) <= 0:
			return render(request, 'user_page/request_page.html', 
			{'message': "ไม่ผมวิชาที่ค้นหา",
			})
		return render(request, 'user_page/request_page.html', 
		{'searched_subjects': search_result,
		})
	return render(request, 'user_page/request_page.html', {
		'selected_subjects': request.session['selected_subjects'],
	})

def acquire_quota(request, sub_id):
	s = Subject.objects.get(pk=sub_id)
	request.session['selected_subjects'] += [[s.subject_id, s.name, s.gpd]]
	print(request.session['selected_subjects'])
	print(type(request.session['selected_subjects']))
	return redirect('./')

def quota_result(request):
	subjects = users.objects.get(username=request.user.username).subjects.all()
	return render(request, 'user_page/request_result.html', 
	{'quota_result': subjects})

def log_out(request):
	if 'selected_subjects' in request.session:
		request.session['selected_subjects'] = []
	logout(request)
	return redirect('login_page:login')


