from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path, include
from .models import Subject, Student
from django import forms

# Create your views here.

def front_page(request):
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
	'time': time_format})
	
class Search_subjects(forms.Form):
	search = forms.CharField(label="ค้นหารายวิชา (รหัสวิชา):", min_length=2)

def quota_page(request):
	search_result = []
	context = {}
	if (request.method == 'POST'):
		sub_id = request.POST['subject_id']	
		search_result += Subject.get_subject(sub_id)
		return render(request, 'user_page/request_page.html', 
		{'searched_subjects': search_result})
	return render(request, 'user_page/request_page.html')
