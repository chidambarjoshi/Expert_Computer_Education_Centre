from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.base import Model
from django.utils.text import slugify


class Course(models.Model):
    "Add or remove courses"
    course_name=models.CharField(max_length=30,verbose_name="Course Name")
    course_description=models.CharField(max_length=300,verbose_name="Course Description")
    


    def __str__(self):
        return self.course_name
import datetime


class Student(models.Model):

    '''Students table '''
    year_dropdown = []
    for y in range(2018, (datetime.datetime.now().year + 10)):
        year_dropdown.append((str(y), str(y)))
    GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'))
    CASTE_CHOICES=(('SC','SC'),('ST','ST'),('OBC','OBC'),('GM','GM'))
    RELIGION_CHOICE=(('Hindu','Hindu'),('Muslim','Muslim'),('Jain','Jain'),('Christian','Christian'))
    year_of_addmission=models.CharField(max_length=4,choices=year_dropdown, default=str(datetime.datetime.now().year))
    role_no=models.CharField(max_length=3,verbose_name='Student Roll NO',default="00",blank=True,null=True)
    stud_name= models.CharField(max_length=30,verbose_name="Student Name",blank=True,null=True)
    student_id=models.CharField(max_length=40,verbose_name="Student ID",blank=True,null=True)
    fat_name= models.CharField(max_length=30,verbose_name="Father Name")
    mat_name= models.CharField(max_length=30,verbose_name="Mother Name")
    email=models.CharField(max_length=60,verbose_name="Email")
    qualification= models.CharField(max_length=20,verbose_name="Qualification")
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True,verbose_name="Gender")
    caste =models.CharField(choices= CASTE_CHOICES,max_length=10,verbose_name="Csate")
    religion = models.CharField(choices=RELIGION_CHOICE, max_length=20,verbose_name="Religion")
    course= models.ForeignKey(Course,on_delete=models.CASCADE)
    des_time= models.TimeField(auto_now= False,verbose_name="Desire Time")
    address=models.TextField(max_length=100,verbose_name="Address")
    stud_number=models.CharField(max_length=11,verbose_name="Student's Number")
    pre_number=models.CharField(max_length=11,verbose_name="Perent's Number")


    def __str__(self):
        return self.stud_name


    def save(self):
        
        self.student_id=str(self.year_of_addmission)+'ECEC'+str(self.role_no)
        print(self.year_dropdown)
        return super().save()