from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Department,Faculty,Student
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email','first_name','last_name']
    search_fields = ['email','first_name','last_name']

admin.site.register(User, CustomUserAdmin)

admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(Student)
