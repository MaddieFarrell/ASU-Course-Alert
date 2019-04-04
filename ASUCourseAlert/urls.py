"""ASUCourseAlert URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from waitlist import views
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('waitlist_sign_up/', views.sign_up_for_waitlist, name='sign_up_for_waitlist'),
    path('semester/', views.get_semesters, name='get_semesters'),
    path('session/', views.get_sessions, name='get_sessions'),
    path('subject/', views.get_subject, name= 'get_subject'),
    path('waitlist/', views.get_students_waitlist, name='get_students_waitlist'),
    path('recovery/', views.pin_recovery, name='pin_recovery'),
    path('', views.empty_view, name='empty_view'),


]

