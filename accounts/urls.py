from django.urls import path 
from .views import student_login_view

urlpatterns = [
    path("login/student",student_login_view,name="student_login_view")
]
