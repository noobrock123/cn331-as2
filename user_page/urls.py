from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "user_page"
urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('quota_request/', views.quota_page, name='quota_request_page'),
    path('acquire_quota/', views.acquire_quota, name='acquire_quota'),
    path('show_quota_result/', views.quota_result, name='show_quota_result'),
	path('logout', views.log_out, name='log_out')
]
