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

def about(request):
	return render(request,'about.html')

def schedule(request):
	return render(request,'schedule.html')

def calender(request):
	return render(request,'calender.html')


def srs(request):
	error=""
	
	if request.method=="POST":
		n=request.POST['t1']
		m=request.POST['t2']
		i=request.POST['t3']
		j=request.POST['t4']
		a=request.POST['card1']
		b=request.POST['card2']
		c=request.POST['card3']
	
		try:
			Srs.objects.create(name=n,email=m,suggestion=i,contact=j,shift=a,meeting=b,overall=c) ##inser command
			error="no"
			
		except:  
			error="yes"
	
	d={'error':error}
	return render(request,'srs.html',d)

def grs(request):
	error=""
	
	if request.method=="POST":
		n=request.POST['t1']
		m=request.POST['t2']
		i=request.POST['t3']
		a=request.POST['card1']
		b=request.POST['detail']
		

		
		try:
			Grs.objects.create(name=n,email=m,contact=i,types=a,detail=b) ##inser command
			error="no"
			
		except:  
			error="yes"
	
	d={'error':error}
	return render(request,'grs.html',d)

def homeal(request):
    return render(request,'homeal.html')

def aboutal(request):
    return render(request,'aboutal.html')

def scheduleal(request):
    return render(request,'scheduleal.html')

def calenderal(request):
    return render(request,'calenderal.html')











# Create your views here.
