from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'user_page'
urlpatterns = [
    path('', views.index),
    path('quota_request/', include('quota_request_page.urls', \
    namespace = "q_request"))
]
