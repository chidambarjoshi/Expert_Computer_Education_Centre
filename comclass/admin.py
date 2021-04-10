from django.contrib import admin
from .models import Student,Course
# Register your models here.
class StudentDisplay(admin.ModelAdmin):
    model=Student
    list_display=('stud_name','course','des_time','stud_number')
    filter=('course','des_time')
    fieldsets = [
        ('Student Details',{'fields':('student_id','stud_name','email','gender','qualification','stud_number','address','course','des_time')}),
        ('Other Details',{'fields':('fat_name','mat_name','caste','religion','pre_number')})
    ]
    pass
admin.site.register(Student , StudentDisplay)

admin.site.register(Course)