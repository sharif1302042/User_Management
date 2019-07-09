from django.urls import path,include

from .views import UserCreation,AssignUserToGroup

urlpatterns = [
    path('user_create/',UserCreation.as_view()),
    path('assign_user_to_group/',AssignUserToGroup.as_view()),

]