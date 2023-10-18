from django.shortcuts import render

from . import forms

# Create your views here.
def StudentRegisterView(request):
    form=forms.StudentRegister()
    if request.method=='POST':
        form=forms.StudentRegister(request.POST)
        if form.is_valid():
            print('Form validation success and printing data')
            print('Name: ', form.cleaned_data['name'])
            print('Roll: ', form.cleaned_data['rollno'])
            print('Student marks: ', form.cleaned_data['marks'])
    return render(request,'newapp/register.html',{'form':form})
def ok(request):
    return render(request,'register.html')
