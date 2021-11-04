from django.contrib.auth.models import User,auth
from django.http import request
from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.core.validators import MinLengthValidator
from django.views import View
from .models import *
from datetime import datetime, timedelta
import calendar
import math
import secrets
from .models import *

from django.db.models import Q
# Create your views here.
def index(request):

    return render(request,'index.html')

def success(request):
	return render(request,'success.html')

def test_index(request):
	return render(request,'test_index.html')


def search(request):
	origin = request.POST['origin']
	destination = request.POST['destination']
	seatclass = request.POST['seatclass']
	departdate = request.POST['depart_date']
	trip_type = request.POST['TripType']
	if request.method=='POST':
		if(trip_type=='2'):
			return_date = request.POST['return_date']
			ticket = Ticket.objects.filter(
			origin__code=origin,
			destination__code=destination,
			seat_class=seatclass,
			depart_date=departdate,
			return_date=return_date
			)
			print(origin,destination,trip_type)
			return render(request,"test_index2.html",{'ticket':ticket})
		elif(trip_type=='1'):
			ticket = Ticket.objects.filter(
				origin__code=origin,
				destination__code=destination,
				seat_class=seatclass,
				depart_date = departdate
			)
			print(origin,destination,trip_type)
			return render(request,"test_index2.html",{'ticket':ticket})

def register_request(request):
	'''from_class = NewUserForm
	template_name = 'register' '''
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		phone = request.POST['phone']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		if User.objects.filter(username=username).exists():
				# messages.info(request,'This username has already been taken!')
				print("This username has already been taken!")
				return redirect('register')
		elif User.objects.filter(email=email).exists():
				# messages.info(request,'This email is already in use! Try another email.')
				print("'This email is already in use! Try another email.'")
				return redirect('register')
		else:
			if password1==password2:
			    regis = User.objects.create_user(username=username,email=email,password=password1,phone=phone)
			    regis.save()
			    print("user created")
			else:
				# messages.info(request, 'Password is not match!')
				print("Password is not match!")
				return redirect('register')
		return redirect('/')
	else:
		return render(request,'register.html')


def login_request(request):
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			messages.success(request, f" Hello {username}, You Are Successfully Logged In")
			return render(request,"success.html")
		else:
			if not User.objects.create_user(username=username).exists():
				messages.error(request, "Username Doesn't Exist")
			else:
				messages.info(request, "Incorrect Password")
			return redirect('/')
	else:
		return render(request,'login.html')

def logout(request):
	auth.logout(request)
	return redirect('/')



        