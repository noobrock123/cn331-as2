from django.db import models

# Create your models here.

class Subject(models.Model):
	subject_code = models.CharField(max_length=5, primary_key=True)
	name = models.CharField(max_length=150)
	gpd = models.CharField(max_length=3)
	def __str__(self):
		return f"{self.subject_code}: {self.name}. GPD: {self.gpd}"

class Students(models.Model):
	student_id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=80)
	subjects = models.ManyToManyField(Subject)
	def __str(self):
		return f"{name} {studednt_id}"
