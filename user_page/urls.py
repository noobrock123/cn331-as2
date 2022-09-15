from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "user_page"
urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('quota_request/', views.quota_page, name='quota_request_page'),
    path('quota_request/get/<str:sub_id>', views.acquire_quota, name='acquire_quota'),
    path('quota_request/remove/<str:sub_id>', views.remove_quota, name='remove_quota'),
    path('quota_request/quota_accept', views.accept_quota, name='accept_quota'),
    path('show_quota_result/', views.quota_result, name='show_quota_result'),
    path('show_quota_result/remove/<str:sub_id>', views.remove_acquired_quota, name='remove_acquired_quota'),
	path('logout', views.log_out, name='log_out')
]
