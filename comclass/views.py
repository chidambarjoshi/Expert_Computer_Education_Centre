from django.http.response import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404 
from .form import StudentAdmissionForm,CourseEdit,UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Course,Student
from .utils import render_to_pdf
import datetime
#from easy_pdf.rendering import render_to_pdf

year_dropdown = []
for y in range(2018, (datetime.datetime.now().year + 10)):
    year_dropdown.append((str(y)))
# Create your views here.
def login_view(request):
    '''
        login for admin 
        Author : Chidambar Joshi

    '''
    if request.user.is_authenticated:
        return redirect('/')
    print("login")
    form = UserLoginForm(request.POST or None)
    next = request.GET.get('next')
    if  request.method == "POST":  
        print("post")      
        if form.is_valid():
            print("valid")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request, user)
                if next:
                    return redirect(next)
                return redirect('/')
    else:
        form = UserLoginForm()
        context = {
                'form': form
            }
        return render(request, "login.html", context)
    

        
  
def home(request):
    '''
            Renders Home page 
            Author : Chidambar
    '''
    return render(request,'home.html')


def courses(request):
    '''
        Display all the courses from the db
        Author : Chidambar Joshi 
    '''
    course=Course.objects.all
    context={'course':course}
    return render(request,'courses.html',context)


def about(request):
    '''
        Renders about page a Static Page
        Author : Chidambar Joshi
    '''
    return render(request,'aboutus.html')


def Addmission(request):
    '''
        Provides from for Student addmission
        Author : Chidambar Joshi
    '''
    
    form = StudentAdmissionForm(request.POST or None)
    context={
        'form':form
    }
    if request.method == "POST":
        if form.is_valid():
            student=form.save(commit=False)
            student.save()
            messages.success(request, 'Admission success..Thank you for your Intrest')
        else:
            print('invalid')
            print(form.errors)
            
    return render(request,'admission.html',context)


@login_required
def student_details(request):
    '''
        Display all the student infomation to admin 
        Access to Admin only
        Author : Chidambar Joshi
    '''
    students= Student.objects.all().order_by('student_id')
    year='all'
    
    if request.method == "POST":
        year=request.POST.get('add_year')
        search=request.POST.get('search')
        print(year)
        if year == 'all':
            students= Student.objects.all().order_by('student_id')
        else :
            students= Student.objects.filter(year_of_addmission=str(year)).order_by('student_id')
        if search :
            students= Student.objects.filter( Q(stud_name__icontains = search) )
        

    context={
        'students':students,
        'year_dropdown':year_dropdown,
        'selected_year':year
    }
    return render(request,'student_details.html',context)

@login_required
def details(request,id):
    '''
        Display the details of students on pk
        Author : Chidambar Joshi

    '''
    student=[] 
    context={}
    try:
        student=get_object_or_404(Student,id=id)
        print(student)
        context={
            'stud':student
        }
    except :
        print("Not found")
        messages.error(request,"Student Not found")
    
   
    return render(request,'details.html',context)



def details_download(request,id):
    '''
        Download the pdf file of student details
        Author : Chidmabar Joshi
    '''
    student=Student.objects.get(id=id)
    context={
        'stud':student
    }
    pdf=render_to_pdf('details1.html',context)
    return HttpResponse(pdf,content_type='application/pdf')


def logout_view(request):
    logout(request)
    return redirect('/')

def course_edit(request,id):
    
    form=""
    if id != '{new}':
        form=CourseEdit(request.POST or None,instance=Course.objects.get(id=id))
    else:
        form=CourseEdit(request.POST or None)
    context={
        "form":form
    }
    if request.method == "POST":
        if form.is_valid():
            course=form.save(commit=False)
            course.save()
            messages.success(request, 'Course Updated')
            return redirect("/course")
        else:
            print("//////invalid//////")
    return render (request,"course_edit.html",context)

def edit_student(request,id):    
    form = StudentAdmissionForm(request.POST or None,instance=Student.objects.get(id=id))
    context={
        'form':form
    }
    if request.method == "POST":
        if form.is_valid():
            student=form.save(commit=False)
            student.save()
            messages.success(request, 'Student Details Updated')
            return redirect("/allstudent")
            
    return render(request,'admission1.html',context)

def course_del(request,id):
    course=Course.objects.get(id=id)
    if course:   
        course.delete() 
        messages.success(request, 'Course Deleted')
        return redirect("/course")
      
def stud_del(request,id):
    stud=Student.objects.get(id=id)
    if stud:
        stud.delete()
        messages.success(request,"Student romved successfully")
        return redirect("/allstudent")

