from django import forms
class StudentRegister(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    marks=forms.IntegerField()
    