from django.shortcuts import render
from django.http import HttpResponse
from .models import get_subject

# Create your views here.
def index(request):
	return HttpResponse('<h1>Test</h1>')

def get_subjects(request, sub_id):
	subjects = get_subject(sub_id)
	pass