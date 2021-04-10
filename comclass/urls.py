from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from .views import home,courses,Addmission,about,student_details,details, details_download,logout_view,course_edit,edit_student,login_view,course_del,stud_del


urlpatterns = [
    path('',home,name='home'),
    path('course',courses,name='course'),
    path('addmission',Addmission,name='addmission'),
    path('about',about,name='about'),
    path('allstudent',student_details,name='alldetails'),
    path('details/<id>/',details,name='details'),
    path('download_details/<id>',details_download,name="download_details"),
    path('courseedit/<id>/',course_edit,name='courseedit'),
    path('studedit/<id>/',edit_student,name='studedit'),
    path('coursedel/<id>',course_del,name='coursedel'),
    path('stud_del/<id>',stud_del,name='studel'),
    path('logout',logout_view,name='logout'),
    path('login',login_view,name='login'),
 

    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)