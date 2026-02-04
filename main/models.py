from django.db import models
# Create your models here.

class College(models.Model):
    college_logo = models.ImageField(upload_to="collegelogo/")
    college_code = models.CharField(max_length=5,unique=True)
    college_name = models.CharField(max_length=100)
    college_address = models.TextField()
    college_principal = models.CharField(max_length=50)
    def __str__(self):
        return self.college_name

class Department(models.Model):
    department_name = models.CharField(max_length=50,unique=True)
    college = models.ForeignKey(College,on_delete=models.CASCADE)
    hod = models.CharField(max_length=50)
    def __str__(self):
        return self.department_name

class Faculty(models.Model):
    fid = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    profilepic = models.ImageField(upload_to="facultyprofilepic")
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    salary = models.IntegerField()
    def __str__(self):
        return self.name

class Student(models.Model):
    profilepic = models.ImageField(upload_to="studentprofiepic/")
    sid = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    dob = models.DateField()
    address = models.CharField(max_length=200)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    college = models.ForeignKey(College,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Staff(models.Model):
    profilepic = models.ImageField(upload_to="staffprofilepic")
    stid = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    college = models.ForeignKey(College,on_delete=models.CASCADE)
    Department = models.ForeignKey(Department,on_delete=models.CASCADE)
    salary = models.IntegerField()
    def __str__(self):
        return self.name