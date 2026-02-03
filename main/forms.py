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
        fields = "__all__"