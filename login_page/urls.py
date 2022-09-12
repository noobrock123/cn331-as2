from django.urls import path, include

from . import views

app_name = "login_page"
urlpatterns = [
	path('', views.index, name='login'),
	path('user_page/', include('user_page.urls')),
]
