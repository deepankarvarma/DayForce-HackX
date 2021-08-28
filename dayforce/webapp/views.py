from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import *

def home(request):
    return render(request,'home.html')



def login(request):
	error1=""
	
	if request.method=="POST":
		n=request.POST['t1']
		
		i=request.POST['t2']
		
		if Register.objects.filter(name=n,password=i) :
			
			error1="no"
		else:  
			error1="yes"
	
	d={'error1':error1}
	return render(request,'login.html',d)


def register(request):
	error=""
	
	if request.method=="POST":
		n=request.POST['t1']
		m=request.POST['t2']
		i=request.POST['t3']
		j=request.POST['t4']
	
		try:
			Register.objects.create(name=n,email=m,password=i,contact=j) ##inser command
			error="no"
			
		except:  
			error="yes"
	
	d={'error':error}
	return render(request,'register.html',d)


def feedback(request):
	error=""
	
	if request.method=="POST":
		n=request.POST['t1']
		m=request.POST['t2']
		i=request.POST['t3']
		j=request.POST['t4']
	
		try:
			Feedback.objects.create(name=n,email=m,suggestion=i,contact=j) ##inser command
			error="no"
			
		except:  
			error="yes"
	
	d={'error':error}
	return render(request,'feedback.html',d)

def more(request):
	return render(request,'more.html')










# Create your views here.
