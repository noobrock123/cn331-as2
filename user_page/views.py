from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import path, include
from .models import Subject
from django import forms
from django.contrib.auth import logout, models

# Create your views here.

users = models.User
def front_page(request):
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
	return render(request, 'user_page/user_page.html', {
	'name': request.user.first_name,
	'time': time_format})
	
class Search_subjects(forms.Form):
	search = forms.CharField(label="ค้นหารายวิชา (รหัสวิชา):", min_length=2)

search_result = []
def quota_page(request):
	if 'selected_subjects' not in request.session:
		request.session['selected_subjects'] = []
	if 'already_acquired' not in request.session:
		request.session['already_acquired'] = False
	n_students = []
	if (request.method == 'POST'):
		sub_id = request.POST['subject_id']	
		search_result = Subject.get_subject(sub_id, request.user.date_joined.year)
		if len(search_result) == 0 or len(sub_id) <= 0:
			return render(request, 'user_page/request_page.html', 
			{'not_found_message': "ไม่พบวิชาที่ค้นหา",
			})
		return render(request, 'user_page/request_page.html', 
			{'searched_subjects': search_result,
			'selected_subjects': request.session['selected_subjects']		
		})
	if request.session['already_acquired']:
		request.session['already_acquired'] = False
		return render(request, 'user_page/request_page.html', {
			'selected_subjects': request.session['selected_subjects'],
			'already_acquired': "คุณเลือกหรือลงทะเบียนวิชานี้ไปแล้ว" 
		})
	else:
		return render(request, 'user_page/request_page.html', {
			'selected_subjects': request.session['selected_subjects'],
		})

def acquire_quota(request, sub_id):
	subjects = users.objects.get(username=request.user.username).subjects.all()
	s = Subject.objects.get(pk=sub_id)
	if s in request.session['selected_subjects'] or s in subjects:
		request.session['already_acquired'] = True
		return redirect('./')
	request.session['selected_subjects'] += [(s.subject_id, s.name, s.gpd)]
	return redirect('./')

def remove_quota(request, sub_id):
	temp = request.session['selected_subjects']
	for sub in temp:
		if sub_id in sub[0]:
			temp.remove(sub)
	request.session['selected_subjects'] = temp
	return redirect('user_page:quota_request_page')	

#In request page
def quota_result(request):
	subjects = users.objects.get(username=request.user.username).subjects.all()
	return render(request, 'user_page/request_result.html', 
	{'quota_result': subjects})

#In front page
def log_out(request):
	if 'selected_subjects' in request.session:
		request.session['selected_subjects'] = []
	logout(request)
	return redirect('login_page:login')


