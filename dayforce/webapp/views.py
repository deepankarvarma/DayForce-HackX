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
		
		try:
			Register.objects.filter(name=n,password=i,) ##inser command
			error1="no"
		except:  
			erro1r="yes"
	
	d={'error1':error1}
	return render(request,'register.html',d)


def register(request):
	error=""
	
	if request.method=="POST":
		n=request.POST['t1']
		m=request.POST['t2']
		i=request.POST['t3']
		j=request.POST['t4']
        k=request.POST['t5']
        l=request.POST['t6']
		try:
			Register.objects.create(name=n,email=m,password=i,contact=j,gender=k,address=l) ##inser command
			error="no"
		except:  
			error="yes"
	
	d={'error':error}
	return render(request,'register.html',d)









# Create your views here.
