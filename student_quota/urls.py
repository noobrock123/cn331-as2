from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login_page.urls')),
    path('user_page/', include('user_page.urls')),
]
