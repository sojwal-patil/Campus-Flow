from django import forms
from .models import Student,Faculty,Staff,Department,College
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student 
        fields = ["profilepic","sid","name","dob","address",]
        widgets = {
            "profilepic" : forms.ClearableFileInput(attrs={"class":"profile-image","type":"file"}),
            "sid" : forms.TextInput(attrs={"class":"studentid","placeholder":"Enter ID"}),
            "name" : forms.TextInput(attrs={"class":"name","placeholder":"Enter Name of Student"}),
            "dob" : forms.DateInput(attrs={"class":"date","type":"date"}),
            "address" : forms.TextInput(attrs={"class":"address","placeholder":"Enter Address"}),
        }

        labels = {
            "profilepic" : "Upload Profile Picture",
            "sid" : "Enter ID",
            "name" : "Enter Full Name",
            "dob" : "Enter Date of Birth",
            "address" : "Enter Your Address"
        }

class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = ["college_logo","college_code","college_name","college_address","college_principal"]
        labels = {
            "college_logo" : "College Logo",
            "college_code" : "Code",
            "college_name" : "Name",
            "college_address" : "Address",
            "college_principal" : "Principal"
        }
        widgets = {
            "college_code" : forms.TextInput(attrs={"placeholder":"Enter College Code"}),
            "college_name" : forms.TextInput(attrs={"placeholder":"Enter College Name"}),
            "college_address" : forms.TextInput(attrs={"placeholder":"Enter Address of College"}),
            "college_principal" : forms.TextInput(attrs={"placeholder":"Enter Name of Principal"})
        }

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ["department_name","hod"]
        labels = {
            "department_name" : "Department Name",
            "hod" : "Head Of Department"
        }
        widgets = {
            "department_name" : forms.TextInput(attrs={"placeholder":"Enter Name of Department"}),
            "hod" : forms.TextInput(attrs={"placeholder":"Enter HOD Name"})
        }