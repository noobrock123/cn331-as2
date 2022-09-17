from django.shortcuts import render, redirect
from django.urls import path, include
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
	if request.method == "POST":
		student_id = request.POST['student_id']
		password = request.POST['password']
		user = authenticate(username=student_id, password=password)
		if user is not None:
			if user.is_superuser:
				login(request, user)
				return redirect('admin/')
			login(request, user)
			return redirect('user_page:front_page')	
		else:
			return render(request, 'login_page/login.html',
			{ 'message': "กรุณาใส่รหัสนักศึกษาและรหัสเข้าระบบให้ถูกต้อง"})
	return render(request, 'login_page/login.html')

