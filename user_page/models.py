from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.

semesters_choice = (
	(1, 1),
	(2, 2),
	(3, 3)
)
year_choice = [(r,r) for r in range(1934, datetime.datetime.now().year + 1)]
class Subject(models.Model):
	subject_id = models.CharField(max_length=5, primary_key=True)
	name = models.CharField(max_length=150, null=False)
	gpd = models.CharField(max_length=3, default="0.0")
	semester = models.IntegerField(choices=semesters_choice, default=1)
	n_seats = models.IntegerField(default=0)
	is_requestable = models.BooleanField(default=False)
	students = models.ManyToManyField(User, related_name="user", blank=True)

	def get_subject(sub_id):
		if type(sub_id) != str:
			print("Error")	
			return []
		else:
			subjects = Subject.objects.filter(subject_id__startswith=sub_id)
			if len(subjects) == 0:
				print("No subject found")	
			else:
				print(f"{len(subjects)} subjects found.")
			return subjects

	def __str__(self):
		return f"{self.subject_id}: {self.name}, Semester: {self.semester},GPD: {self.gpd}, Seats= {self.n_seats}"

class Year(models.Model):
	year = models.IntegerField(choices=year_choice, default=datetime.datetime.now().year, primary_key=True)
	subjects = models.ManyToManyField(Subject, blank=True, related_name="subjects")

	def __str__(self):
		return f"Year: {self.year}"
#class Student(models.Model):
#	student_id = models.IntegerField(primary_key=True)
#	name = models.CharField(max_length=80, null=False)
#	subjects = models.ManyToManyField(Subject, blank=True, related_name="students")
#	def __str(self):
#		return f"{name} {studednt_id}"
