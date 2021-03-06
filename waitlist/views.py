from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from waitlist.models import StudentPin
from waitlist.models import Course
from waitlist.models import WaitingStudent
from waitlist.models import Semester
from django.core import serializers
from waitlist.subjects import subjects
import requests
import json


@csrf_exempt
def sign_up_for_waitlist(request):
	if request.method == "POST":
		json_date = json.loads(request.body)
		email = json["email"]
		pin = json["pin"]
		student_pin = StudentPin.objects.get(email = email)
		if student_pin.exists():
			if student_pin.pin == json_data["pin"]:
				course = Course.objects.get(semester=json_data["semester"], subject_name=json_data["subject_name"], subject_number=json_data["subject_number"], session=json_data["session"],):
					if course.exists():
						qs_json = serializers.serialize("json", course)
							return(qs_json)
					else:
						created_course = Cousrse.objects.create(
							semester=json_data["semester"],
							subject_name=json_data["subject_name"],
							subject_number=json_data["subject_number"],
							session=json_data["session"],
							)
							qs_json = serializers.serialize("json", created_course)
								return HttpResponse(qs_json)
			return HttpResponse("Error! Please enter the correct pin number")
		else:
			create_student_pin = StudentPin.objects.create(
				email = json_data["email"],
				pin = json_date["email"],
				)
			course = Course.objects.get(semester=json_data["semester"], subject_name=json_data["subject_name"], subject_number=json_data["subject_number"], session=json_data["session"],):
				if course.exists():
					qs_json = serializers.serialize("json", course)
						return HttpResponse(qs_json)
				else:
				created_course = Course.objects.create(
					semester=json_data["semester"],
					subject_name=json_data["subject_name"],
					subject_number=json_data["subject_number"],
					session=json_data["session"],
					)
					qs_json = serializers.serialize("json", created_course)
						return HttpResponse(qs_json)
	return HttpResponse("Error")


@csrf_exempt
def get_semesters(request):
	if request.method == "GET": 
		semesters = Semester.objects.all() 
		qs_json = serializers.serialize("json", semesters) 
		return HttpResponse(qs_json)
	return HttpResponse("Error")


@csrf_exempt
def get_sessions(request):
	if request.method == "GET":
		sessions = ["A", "B", "C", "DYN"] 
		qs_json = serializers.serialize("json", sessions)
		return HttpResponse(qs_json) 
	return HttpResponse("Error")


@csrf_exempt
def get_subject(request):
	if request.method == "GET":
		qs_json = serializers.serialize("json", subjects)	
		return HttpResponse(qs_json)
	return HttpResponse("Error")


@csrf_exempt
def get_students_waitlist(request):
	if request.method == "GET":
		email = request.GET.get("email", "")#url that they pass in, we extract the email and pin from the url
		pin = request.GET.get("pin", "")
		if StudentPin.objects.get(email=email, pin=pin).exists():
			student_courses = []
			for row in WaitingStudent.objects.filter(email=email, sent=False): # grab rows that match the case, double for loop
				student_courses.append(row.course) # only added 1 class
				qs_json = serializers.serialize("json", student_courses)
				return HttpResponse(qs_json)
		return HttpResponse("Please Enter your correct pin number and email")
	return HttpResponse("Error")

@csrf_exempt
def pin_recovery(request):
	if request.method == "POST":
		return HttpResponse("Your pin number is %s." % pin)
#TODO: send pin to the email










#.get = looks through all rows of the table, the 1st one
#.filter = all rows emails adn return what it matches - return models.






