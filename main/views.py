from django.shortcuts import render,redirect
from .forms import StudentForm,CollegeForm
from .models import Student,College
# Create your views here.

def index(request):
    colleges = College.objects.all()
    context = {
        "colleges" : colleges
    }
    return render(request,"index.html",context)

def addcollege(request):
    college_form = CollegeForm()
    if request.method == "POST":
        college_form = CollegeForm(request.POST,request.FILES)
        if college_form.is_valid():
            college_form.save()
            return redirect("index")
        
    context = {
        "college_form" : college_form
    }
    return render(request,"addcollege.html",context)

def addstudent(request):
    student_form = StudentForm()
    students = Student.objects.all()
    if request.method == "POST":
        student_form = StudentForm(request.POST,request.FILES)
        if student_form.is_valid():
            student_form.save()
            return redirect("index")
        
    context = {
        "student_form" : student_form,
        "students" : students,
    }
    return render(request,"addstudent.html",context)