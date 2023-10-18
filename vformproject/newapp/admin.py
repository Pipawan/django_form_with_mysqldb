from django.contrib import admin
from newapp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','rollno','marks']

admin.site.register(Student,StudentAdmin)
