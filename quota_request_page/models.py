from django.db import models

# Create your models here.

def get_subject(sub_id):
	if type(sub_id) != str:
		print("Error")	
	else:
		if len(sub_id) == 2:
			subjects = Subject.objects.filter(subject_id__startswith=sub_id)
			if len(subjects) == 0:
				print("No subject found")	
			else:
				print(f"{len(subjects)} subjects found.")
			return subjects

class Subject(models.Model):
	subject_id = models.CharField(max_length=5, primary_key=True)
	name = models.CharField(max_length=150, null=False)
	gpd = models.CharField(max_length=3, default="0.0")
	n_seats = models.IntegerField(default=0)
	ocu_seats = models.IntegerField(default=0)
	def __str__(self):
		return f"{self.subject_id}: {self.name}. GPD: {self.gpd} / Seats= {self.n_seats}/{self.ocu_seats}"

class Student(models.Model):
	student_id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=80, null=False)
	subjects = models.ManyToManyField(Subject)
	def __str(self):
		return f"{name} {studednt_id}"
