from django.urls import path,include

from .views import UserCreation

urlpatterns = [
    path('user-create/',UserCreation.as_view()),

]