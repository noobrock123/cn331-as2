from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	from django.utils import timezone
	hour = timezone.localtime().hour
	minute = timezone.localtime().minute
	time_format = ""
	if hour >= 0 and hour < 11:
		if hour == 0:
			hour = 12
		time_format = "AM"
	elif hour >=12 and hour <= 23:
		hour = hour % 12
		time_format = "PM"
	if minute < 10:
		time_format = str(hour) + ":0" + str(minute) + time_format
	else:
		time_format = str(hour) + ":" + str(minute) + time_format
	return render(request, 'user_page/user_page.html', {
	'time': time_format})
