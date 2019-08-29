
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('User_Management.urls')),
    path('auth/',include('token_auth.urls')),
]
