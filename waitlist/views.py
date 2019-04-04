from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from waitlist.models import StudentPin
from waitlist.models import Course
from waitlist.models import WaitingStudent
from waitlist.models import Semester
from django.core import serializers
import requests
import json

# Create your views here.
@csrf_exempt
def sign_up_for_waitlist(request):
	if request.method == 'POST':
		json_data == json.loads(request.body)
		student_waitlist = Course.StudentPin.objects.create(
			semester=json_data["semester"],
			subject_name=json_data["subject_name"],
			subject_number=json_data["subject_number"],
			session=json_data["session"],
			email=json_data["email"],
			pin=json_data["pin"],
		)
		return HttpResponse(student_waitlist)
	return HttpResponse("Error")

@csrf_exempt
def get_semesters(request):
	if request.method == 'GET':
		course_semesters = request.GET.get('semester', ' ')
		qs_json = serializers.serialize('json', Semester.objects.filter(semester=semester))
	return HttpResponse(qs_json)

@csrf_exempt
def get_sessions(request):
	if request.method == 'GET':
		sessions = request.GET.get('session', ' ')
		qs_json = serializers.serialize('json', Course.objects.filter(session=session))	
	return HttpResponse(qs_json)

@csrf_exempt
def get_subject(request):
	if request.method == 'GET':
		subjects = request.GET.get('subject', ' ')
		qs_json = serializers.serialize('json', Course.objects.filter(subject_name=subject_name, subject_number=subject_number))	
	return HttpResponse(qs_json)

@csrf_exempt
def get_students_waitlist(request):
	if request.method == 'GET':
		email = request.GET.get('email', ' ')
		if StudentPin.objects.filter(email=email).exists():
			if email == pin:
				return HttpResponse(students_waitlist)
		return("Error")

@csrf_exempt
def pin_recovery(request):
	if request.method == 'POST':
		return HttpResponse("Your pin number is %s." % pin)
#TODO: send pin to the email
@csrf_exempt
def empty_view(request):
    return HttpResponse("Empty View")











