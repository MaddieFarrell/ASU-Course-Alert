from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from waitlist.models import StudentPin
from waitlist.models import Course
from waitlist.models import WaitingStudent
from waitlist.models import Semester
import requests
import json

# Create your views here.
@csrf_exempt
def sign_up_for_waitlist(request):
	if request.method == 'POST':
		json_data == json.loads(request.body)
		account = Course.StudentPin.objects.create(
			semester=json_data["semester"],
			subject_name=json_data["subject_name"],
			subject_number=json_data["subject_number"],
			session=json_data["sessionr"],
			email=json_data["email"],
			pin=json_data["pin"],
		)
		return HttpResponse(pin)
	return HttpResponse("Error")

@csrf_exempt
def get_semesters(request):
	if request.method == 'GET':
		course_semesters = Course.objects.get(semester)
		response = "Semester: "
		for semesters in course_semesters:
	 		response += " " + semesters.semester + " "
	return HttpResponse(response)

@csrf_exempt
def get_sessions(request):
	if request.method == 'GET':
		sessions = Course.objects.get(session)
		response = "Session: "
		for sesh in sessions:
			response += " " + sesh.session + " "
	return HttpResponse(response)

@csrf_exempt
def get_subject(request):
	if request.method == 'GET':
		subjects = Course.objects.get(subject_name, subject_number)
		response = "Subject: "
		for subject in subjects:
			response += " " + subject.subject_name + subject.subject_number + " "
	return HttpResponse(response)

@csrf_exempt
def get_students_waitlist(request):
	if request.method == 'GET':
		students_waitlist = Course.objects.all()
		response = "You're waiting on: "
		for classes in students_waitlist:
			response += " " + classes.subject_name + " , " + classes.session + " , " + classes.subject_number + " , " + classes.semester + " "
	return HttpResponse(response)


@csrf_exempt
def pin_recovery(request):
	if request.method == 'POST':
		return HttpResponse("Your pin number is %s." % pin)
#TODO: send pin to the email






