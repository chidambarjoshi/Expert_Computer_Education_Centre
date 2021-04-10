from django import forms
from django.db.models import fields
from django.contrib.auth import authenticate
from .models import Student,Course



class StudentAdmissionForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['year_of_addmission','role_no','stud_name','email','gender','qualification',
        'stud_number','address','course','des_time','fat_name',
        'mat_name','caste','religion','pre_number']
        widgets ={
            'year_of_addmission':forms.Select(attrs={'class': "form-control",}) ,
            'role_no':forms.TextInput(attrs={'class': "form-control",'placeholder':'Roll Number'}),
            'stud_name' : forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Student Name'}) ,
            'email' : forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Email Id'}) ,
            'gender' : forms.Select(attrs={'class': "form-control", 'placeholder': 'Gender'}),
            'qualification':forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Qualification'}),
            'des_time': forms.TimeInput(attrs={'class': "form-control", 'type': 'time', 'placeholder': 'Desire Time'}),
            'stud_number':forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Student Mobile Number'}),
            'address': forms.Textarea(attrs={'class': "form-control",  'placeholder': 'Address' , 'style ':'height:45px;'}),
            'course' : forms.Select(attrs={'class': "form-control", 'placeholder': 'Select Course'}),
            'fat_name' : forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Father Name'}) ,
            'mat_name' : forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Mother Name'}) ,
            'caste' : forms.Select(attrs={'class': "form-control", 'placeholder': 'Select Caste'}),
            'religion' : forms.Select(attrs={'class': "form-control", 'placeholder': 'Select Religion'}),
            'pre_number':forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Perents Mobile Number'})

            
            
        }

    
   


class CourseEdit(forms.ModelForm):
    class Meta:
        model=Course
        fields=['course_name','course_description']
        widgets ={
            'course_name' : forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Course Name'}) ,
            'course_description' : forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Description'}) ,}
        def clean(sefl,*args, **kwargs):
            course_name=self.cleaned_data.get('course_name')
            course_description=self.cleaned_data.get('course_description')
            return super(CourseEdit, self).clean(*args, **kwargs)

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput() )
    widgets ={
        'username':forms.TextInput(attrs={'class': "form-control", 'placeholder': 'UserName'})
    }


    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)