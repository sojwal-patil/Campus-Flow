#Shortcuts
from django.shortcuts import render,redirect

#Forms
from .forms import LoginForm

# Contrib
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Models 
from .models import User

#Exceptions
from django.core.exceptions import BadRequest

def student_login_view(request):
    student_login_form = LoginForm()
    if request.method == "POST":
        if student_login_form.is_valid():
            email = student_login_form.cleaned_data["email"]

            password = student_login_form.cleaned_data["password"]

            user = authenticate(email=email,password=password)

            if user is not None:
                login(request,user)
            else:
                messages.error(request,"User does not exist",extra_tags="usererror")
            
    context = {
            "student_login_form" : student_login_form
        }

    return render(request,"login/student.html",context)


def logout(request):
    logout(request)