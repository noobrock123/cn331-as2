from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('quota_request_page/', include('quota_request_page.urls'))
    
]
