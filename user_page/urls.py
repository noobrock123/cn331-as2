from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "user_page"
urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('quota_request/', views.quota_page, name='quota_request_page'),
	path('logout', views.log_out, name='log_out')
]
