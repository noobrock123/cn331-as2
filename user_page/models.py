from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Subject(models.Model):
	subject_id = models.CharField(max_length=5, primary_key=True)
	name = models.CharField(max_length=150, null=False)
	gpd = models.CharField(max_length=3, default="0.0")
	n_seats = models.IntegerField(default=0)

	def get_subject(sub_id):
		if type(sub_id) != str:
			print("Error")	
		else:
			subjects = Subject.objects.filter(subject_id__startswith=sub_id)
			if len(subjects) == 0:
				print("No subject found")	
			else:
				print(f"{len(subjects)} subjects found.")
			return subjects

	def __str__(self):
		return f"{self.subject_id}: {self.name}. GPD: {self.gpd} / Seats= {self.n_seats}/{self.ocu_seats}"

class Student(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	student_id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=80, null=False)
	subjects = models.ManyToManyField(Subject, blank=True, related_name="students")
	def __str(self):
		return f"{name} {studednt_id}"
