from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("" , views.index,name="index"),
    # path("addstudent",views.addstudent,name="addstudent"),
    path("<str:college_name>",views.college,name="college"),
    path("<str:college_name>/<str:department_name>",views.department,name="department")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)