from django.contrib import admin
from .models import College,Department,Faculty,Student,Staff
# Register your models here.

admin.site.register(College)
admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Staff)
