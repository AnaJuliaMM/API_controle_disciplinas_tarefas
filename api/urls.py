"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views.students.studentView import StudentView
from .views.students.studentsDetailView import StudentDetailView
from .views.subjects.subjectView import SubjectView
from .views.subjects.subjectDetailView import SubjectDetailView
from .views.tasks.taskView import TaskView
from .views.tasks.taskDetailView import TaskDetailView
from .views.student_taks.studentTaskView import StudentTaskView



urlpatterns = [
    path('students/', StudentView.as_view()),
    path('students/<int:pk>/', StudentDetailView.as_view()),
    path('subjects/', SubjectView.as_view()),
    path('subjects/<int:pk>/', SubjectDetailView.as_view()),
    path('tasks/', TaskView.as_view()),
    path('tasks/<int:pk>/', TaskDetailView.as_view()),
    path('student/<int:pk>/tasks/', StudentTaskView.as_view()),

]
