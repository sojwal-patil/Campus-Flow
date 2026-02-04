from django.shortcuts import render,redirect,get_object_or_404
from .forms import StudentForm,CollegeForm,DepartmentForm
from .models import Student,College,Department
# Create your views here.

def index(request):
    colleges = College.objects.all().order_by("-id")
    college_form = CollegeForm()
    if request.method == "POST":
        college_form = CollegeForm(request.POST,request.FILES)
        if college_form.is_valid():
            college_object = college_form.save()
            return redirect("college",college_name=college_object.college_name)
    context ={
        "colleges" : colleges,
        "college_form" : college_form

    }
    return render(request,"index.html",context)

def college(request,college_name):

    department_form = DepartmentForm()
    college = get_object_or_404(College,college_name=college_name)
    departments = Department.objects.filter(college__college_name=college_name)

    if request.method == "POST":
        department_form = DepartmentForm(request.POST)
        if department_form.is_valid():
            dept = department_form.save(commit=False)
            dept.college = college
            dept.save()
            return redirect("college",college_name=college.college_name)
        

    context = {
        "college":college,
        "department_form":department_form,
        "departments" : departments
    }

    return render(request,"college.html",context)

def department(request, college_name, department_name):
    students = Student.objects.all().filter(department__department_name=department_name)
    college = College.objects.get(college_name=college_name)
    department = Department.objects.get(department_name=department_name)
    student_form = StudentForm()

    if request.method == "POST":
        student_form = StudentForm(request.POST,request.FILES)
        if student_form.is_valid():
            student_object = student_form.save(commit=False)
            student_object.college = college          # ✅ FIX
            student_object.department = department    # ✅ FIX
            student_object.save()
            return redirect(
                "department",
                college_name=college.college_name,
                department_name=department.department_name
            )

    return render(request, "department.html", {
        "college": college,
        "department": department,
        "student_form": student_form,
        "students" : students,
    })