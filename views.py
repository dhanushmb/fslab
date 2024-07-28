#currenttime1
#myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse 
from datetime import datetime
def current_datetime(request):
    now = datetime.now()
    html = f"<html><body><h1>Current Date and Time:</h1><p>{now}</p></body></html>"
    return HttpResponse(html)


#myapp/urls.py 
from django.urls import path 
from . import views 
urlpatterns = [ 
path('current_datetime/', views.current_datetime, name='current_datetime'), 
]

#myproject/urls.py 
from django.contrib import admin 
from django.urls import path, include 
urlpatterns = [ path('admin/', admin.site.urls), 
path('myapp/', include('myapp.urls')), 
] 


#http://127.0.0.1:8000/myapp/current_datetime/

#4hrsahead2
#myapp/views.py 
from django.http import HttpResponse 
from datetime import datetime, timedelta
def datetime_with_offsets(request):
    now = datetime.now() 
    offset_hours= 4
    four_hours_ahead = now + timedelta(hours=offset_hours) 
    four_hours_before =now - timedelta(hours=offset_hours)
    html = f"<html><body><h1>Current Date and Time with Offsets:</h1>" \
    f"<p>Current: {now}</p>" \
    f"<p>Four Hours Ahead: {four_hours_ahead}</p>" \
    f"<p>Four Hours Before: {four_hours_before}</p></body></html>"
    return HttpResponse(html)


#myapp/urls.py 
from django.urls import path 
from . import views 
urlpatterns = [ 
path('datetime_offsets/', views.datetime_offsets, name='datetime_offsets'), 
] 

#myproject/urls.py 
from django.contrib import admin 
from django.urls import path, include 
urlpatterns = [ path('admin/', admin.site.urls), 
path('myapp/', include('myapp.urls')), 
]

#http://127.0.0.1:8000/myapp/datetime_with_offsets/ 

#studentfruit3
#myapp/models.py 
from django.db import models 
class Fruit(models.Model): 
    name = models.CharField(max_length=100) 
    def str (self): 
        return self.name 
class Student(models.Model): 
    name = models.CharField(max_length=100) 
    event = models.CharField(max_length=100) 
    selected = models.BooleanField(default=False) 
    def str (self): 
        return self.name 
#myapp/templates/showlist.html 
<html> 
<style type ="text/css"> 
#i1 {background-color: lightgoldenrodyellow; color: brown; display: table} 
#i2 {background-color: black;color: cyan; display: table} 
</style> 
<body> 
<h1 id ="i1"> Unordered list of fruits </h1> 
<ul> 
{%for fruit in fruits%} 
<li> {{ fruit }}</li> 
{%endfor%} 
</ul> 
<h1 id ="i2"> Ordered list of students </h1> 
<ol> 
{%for student in students%} 
<li> {{ student }}</li> 
{%endfor%} 
</ol> 
</body> 
</html>

#myapp/admin.py 
from django.contrib import admin 
from .models import Fruit, Student 
admin.site.register(Fruit) 
admin.site.register(Student) 
>> python manage.py makemigrations 

#myapp/views.py 
from django.shortcuts import render 
from datetime import date 
from django.http import HttpResponse 
from django.template import Context, Template 
def showlist(request): 
    fruits = ["Grapes", "Orange", "Banana", "Jackfruit"] 
    students = ["Nemo", "Riya","Yoomfi","Nini"] 
    return render(request, 'showlist.html', {"fruits":fruits, "students": students}) 
#myapp/urls.py 
from django.urls import path 
from . import views 
urlpatterns = [ 
path('showlist/', views.showlist, name='showlist'), 
] 
#myproject/urls.py 
from django.contrib import admin 
from django.urls import path, include 
urlpatterns = [ path('admin/', admin.site.urls), 
path('myapp/', include('myapp.urls')), 
]
#http://127.0.0.1:8000/myapp/showlist/

#homepage4
# myapp/templates/layout.html 
<html> 
<title>{% block title %} {% endblock %} </title> 
<style type="text/css"> 
nav { 
background-color: lightblue; 
padding: 10px 
} 
</style> 
<body> 
<nav> 
<a href="/home/">Home</a>| 
<a href="/about_us/">About Us</a>| 
<a href="/contact_us/">Contact Us</a>| 
</nav> 
<section> 
{% block content %} 
{% endblock %} 
</section> 
<footer> 
<hr> 
&copy; CSE, Developed by CSE RVITM. 
</footer> 
</body> 
</html> 
#myapp/templates/home.html 
{% extends 'layout.html' %} 
{% block title %} 
Home 
{% endblock %} 
{% block content %} 
<h2>This is my home page!</h2> 
{% endblock %}

#myapp/templates/about_us.html 
{% extends 'layout.html' %} 
{% block title %} 
Contact us 
{% endblock %} 
{% block content %} 
<h2>Out phone: 134340613 <br> 
Address: bengaluru </h2> 
{% endblock %} 

#myapp/templates/contact_us.html 
{% extends 'layout.html' %} 
{% block title %} 
About Us 
{% endblock %} 
{% block content %} 
<h2>We are DJango developers</h2> 
{% endblock %} 

#myapp/views.py 
from django.shortcuts import render 
from datetime import date 
from django.http import HttpResponse 
from django.shortcuts import render 
from django.template import Context, Template 
def home(request): 
    return render(request,'home.html') 
def about_us(request): 
    return render(request,'about_us.html') 
def contact_us(request): 
    return render(request,'contact_us.html') 
#myapp/urls.py 
from django.urls import path 
from . import views 
urlpatterns = [ 
path('home/', views.home, name='home'), 
path('about_us/', views.about_us, name='about_us'), 
path('contact_us/', views.contact_us, name='contact_us'),]

#myproject/urls.py 
from django.contrib import admin 
from django.urls import path, include 
urlpatterns = [ path('admin/', admin.site.urls), 
path('myapp/', include('myapp.urls')), 
] 

#http://127.0.0.1:8000/myapp/home/ 

#registration5
#myapp/models.py 
from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Course(models.Model):
    name=models.CharField(max_length=100)
    students = models.ManyToManyField(Student)
    def __st__(self):
        return self.name


#myapp/admin.py: 
from django.contrib import admin 
from .models import Course, Student 
admin.site.register(Course) 
admin.site.register(Student) 

#myapp/templates/myapp/register_student.html 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="'viewport" content="'width=device-width,inital-scale=0.1">
    <title>Register Students</title>
</head>
<body>
    <div class="container">
        <h2>Register Student to a course</h2>
        <form action="{% url 'register_student' %}" method="post">
        {% csrf_token %}
        <div class=""label>
            <label for="student_name" class="form_label">Student Name:</label>
            <input type="text" class="from_control" placeholder="Enter your name" id="student_name" name="student_name" required>
        </div>
        <div class="label">
            <label for="course_id" class="'form_label">Select Course</label>
            <select name="course_id" id="course_id" class="form_select" required>
                {% for course in courses %}
            <option value="{{course_id}}">{{course.name}}</option>
            {% endfor %}
            </select>
        </div>
        <button type="submit">Register</button>
        </form>
    </div>
</body>
</html>

#myapp/templates/myapp/course_detail.html 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Course Details</title>
</head>
<body>
    <div>
        <h2>Course Details:{{course.name}}</h2>
    </div>
    <div>
        <h5>Course ID :{{course.id}}</h5>
        <p>Enrolled Students</p>
        <ul>
            {% for student in course.student.all %}
            <li>{{student.name}}</li>
            {% empty%}
            <li>No students Enrolled</li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>

#myapp/views.py 
from django.shortcuts import render, redirect
from .models import Course, Student
from django.urls import reverse
def register_student(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        course_id = request.POST.get('course_id')
        if not course_id:
            return render(request, 'myapp/register_student.html', {'courses': Course.objects.all(), 'error': 'Course ID cannot be empty'})
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return render(request, 'myapp/register_student.html', {'courses': Course.objects.all(), 'error': 'Invalid course ID'})
        student = Student.objects.create(name=student_name)
        course.students.add(student)
        return redirect(reverse('course_detail', args=(course_id,)))
    courses = Course.objects.all()
    return render(request, 'myapp/register_student.html', {'courses': courses})
def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    students = course.students.all()
    return render(request, 'myapp/course_detail.html', {'course': course, 'students': students})

#myapp/urls.py 
from django.urls import path
from .views import register_student,course_detail

urlpatterns=[
    path('register_student/',register_student,name='register_student'),
    path('course_detail/<int:course_id>/',course_detail,name='course_detail')
    ]

#myproject/urls.py 
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls')),
    ]

#python manage.py makemigrations
#python manage.py migrate
#python manage.py createsuperuser
#http://127.0.0.1:8000/admin/
#http://127.0.0.1:8000/register_student/

#6 
#myapp/admin.py change only
from django.contrib import admin
from .models import Course,Student

admin.site.register(Course)
admin.site.register(Student)
class CourseAdmin(admin.ModelAdmin):
    list_display=('name','list_students')
    def list_students(self,obj):
        return ",".join([student.name for student in obj.students.all()])

#7 student,project
#myapp/views.py
from django.shortcuts import render, redirect,get_object_or_404
from .models import Project, Student
from .forms import StudentForm,ProjectForm
def register_student(request):
    if request.method == 'POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form=StudentForm()
        return render(request,'register_student.html',{'form':form})
def add_project(request):
    if request.method == 'POST':
        form=ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form=ProjectForm()
        return render(request,'myapp/add_project.html',{'form':form})
def project_list(request):
    projects=Project.objects.all()
    return render(request,'myapp/project_list.html',{'projects':projects})

def project_detail(request,pk):
    project= get_object_or_404(Project, pk=pk)
    return render(request,'myapp/project_detail.html',{'project':project})

#myapp/models.py
from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Project(models.Model):
    students = models.ForeignKey(Student,related_name='projects', on_delete=models.CASCADE)
    topic= models.CharField(max_length=200)
    languages= models.CharField(max_length=100)
    duration= models.IntegerField(help_text="duration in days")
    def __str__(self):
        return f"{self.topic} by {self.students.name}"

#myapp/forms.py
from django import forms
from .models import Student,Project

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields=['topic','languages','duration','students']

#myapp/urls.py
from django.urls import path
from .views import add_project,project_detail,project_list

urlpatterns=[
    path('add/',add_project,name='add_project'),
    path('',project_list,name='project_list'),
    path('myapp/<int:pk>',project_detail,name='project_detail'),
    ]

#myapp/admin.py
from django.contrib import admin
from .models import Project,Student

admin.site.register(Project)
class ProjectInLine(admin.TabularInline):
    model=Project
    extra=1

class StudentAdmin(admin.ModelAdmin):
    list_display=('name',)
    inlines=[ProjectInLine]

admin.site.register(Student,StudentAdmin)

#templates/myapp/add_project.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Projectt</title>
</head>
<body>
    <h1>Add a new Project</h1>
    <form method="post">
        {% csrf_token %}
        {{form.as_p}}
        <button type="submit">Submit</button>
    </form>
    
</body>
</html>

#templates/myapp/project_detail.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Details</title>
</head>
<body>
    <h1>Project : {{project.topic}}</h1>
    <p><strong>Languages:</strong>{{project.languages}}</p>
    <p><strong>Duration:</strong>{{project.duration}}</p>
    <p><strong>Student:</strong>{{project.students.name}}</p>
</body>
</html>

#templates/myapp/project_list.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project List</title>
</head>
<body>
    <h1>Project List</h1>
    <ul>
        {% for project in projects %}
        <li><a href="{% url 'project_detail' pk=project.pk %}">{{project.topic}}</a></li>
        {% endfor %}
    </ul>
    
</body>
</html>

#makemigrations,migrate,runserver
#/add,/admin

#8 studentlist
#myapp/models.py
from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Course(models.Model):
    name=models.CharField(max_length=100)
    students = models.ManyToManyField('Student',related_name='courses')
    def __str__(self):
        return self.name
#myapp/urls.py
from django.urls import path
from .views import StudentListView,StudentDetailView

urlpatterns=[
    path('myapp/',StudentListView.as_view(),name='student-list'),
    path('myapp/<int:pk>/',StudentDetailView.as_view(),name='student-detail')
    ]

#myapp/views.py
from django.shortcuts import render
from .models import Student
from django.views.generic import ListView,DetailView

class StudentListView(ListView):
    model=Student
    template_name='myapp/student_list.html'
    context_object_name='students'

class StudentDetailView(DetailView):
    model=Student
    template_name='myapp/student_detail.html'
    context_object_name='students'

#myapp/admin.py
from django.contrib import admin 
from .models import Course, Student 
admin.site.register(Course) 
admin.site.register(Student)

#templates/myapp//student_detail.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Details</title>
</head>
<body>
    <h1>Student Details</h1>
    <p>Name:{{student.name}}</p>
</body>
</html>

#templates/myapp//student_list.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Lists</title>
</head>
<body>
    <h1>Student Lists</h1>
    <ul>
        {% for student in students %}
        <li><a href="{% url 'student_detail' pk=student.pk}">{{student.name}}</a></li>
        {% endfor %}
    </ul>
</body>
</html>