from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    user_id = models.CharField(max_length=10,unique=True)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10)
    alternate_number = models.CharField(max_length=10,null=True,blank=True)

    class Role(models.TextChoices):
        SUPER_ADMIN = 'superadmin','SuperAdmin',
        ADMIN = 'admin','Admin'
        PRINCIPAL = ' principal','Principal'
        HOD = 'hod','HOD'
        FACULTY = 'faculty','Faculty'
        STUDENT = 'student','Student'

    role = models.CharField(choices=Role.choices,max_length=10,default=Role.STUDENT)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.email} @ {self.first_name} {self.last_name}"

class Department(models.Model):
    name = models.CharField(max_length=50)
    intake = models.IntegerField()

class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_hod = models.BooleanField(default=False)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    class Section(models.TextChoices):
        A = 'a' , 'A'
        B = 'b' , 'B'
        C = 'c' , 'C'
        D = 'd' , 'D'  
        E = 'e' , 'E'
        F = 'f' , 'F'

    section = models.CharField(choices=Section.choices,default=Section.A,max_length=1)