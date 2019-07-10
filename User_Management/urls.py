from django.urls import path,include

from User_Management import views

urlpatterns = [
    path('user_create/',views.UserCreation.as_view()),
    path('assign_user_to_group/',views.AssignUserToGroup.as_view()),
    path('check_user_group/',views.CheckUserGroup.as_view()),
    path('remove_user_from_group/',views.RemoveUserFromGroup.as_view()),

]