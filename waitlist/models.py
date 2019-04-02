from django.db import models

# Create your models here.
SESSION_CHOICES = (
	("A", "A"),
	("B", "B"),
	("C", "C"),
	("DYN", "DYN"),
)


class StudentPin(models.Model):
	pin = models.IntegerField(max_length=6)
	email = models.CharField(max_length=30)

class Course(models.Model):
	semester = models.CharField(max_length=6)
	subject_name = models.CharField(max_length=8)
	subject_number = models.IntegerField(max_length=8)
	session = models.CharField(max_length=3, choices=SESSION_CHOICES)

class WaitingStudent(models.Model):
	email = models.CharField(max_length=30)
	sent = models.BooleanField(default=False)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Semester(models.Model):
	semester = models.CharField(max_length=6)
	semester_number = models.IntegerField(max_length=6)