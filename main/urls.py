from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("" , views.index,name="index"),
    path("addcollege",views.addcollege,name="addcollege"),
    path("addstudent",views.addstudent,name="addstudent"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)