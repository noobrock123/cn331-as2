from django.contrib import admin
from .models import Subject, Year
# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
    filter_horizontal = ['subjects']

admin.site.register(Subject)
admin.site.register(Year, SubjectAdmin)