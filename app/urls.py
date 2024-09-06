from django.urls import path
from .views import task_list, user_login



urlpatterns = [
    path("", task_list, name="task_list"),
    path("login", user_login, name='login'),
]
