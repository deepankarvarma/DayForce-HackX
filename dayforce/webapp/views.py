from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

def home(request):
    return render(request,'home.html')



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

# Create your views here.
