from django.contrib.auth.models import User,auth
from django.http import request,HttpResponseRedirect
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

def showlocation(request):
	location = Location.objects.all()
	return render(request,{'location':location})

def search(request):
	if request.method=='POST':
		origin = request.POST['origin']
		destination = request.POST['destination']
		seatclass = request.POST['seatclass']
		departdate = request.POST['depart_date']
		returndate = None
		trip_type = request.POST['TripType']
		if(trip_type=='2'):
			return_date = request.POST['return_date']
			ticket = Ticket.objects.filter(
			origin__code=origin,
			destination__code=destination,
			seat_class=seatclass,
			depart_date=departdate,
			return_date=return_date
			)
			print("2",origin,destination,trip_type)
		elif(trip_type=='1'):
			ticket = Ticket.objects.filter(
				origin__code=origin,
				destination__code=destination,
				seat_class=seatclass,
				depart_date = departdate,
				return_date = returndate
			)
			print("1",origin,destination,trip_type)
	return render(request,"searching.html",{'ticket':ticket})

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
				#messages.info(request,'This username has already been taken!')
				print("This username has already been taken!")
				return render(request,'register.html',{'message1':"This username has already been taken"})
		elif User.objects.filter(email=email).exists():
				# messages.info(request,'This email is already in use! Try another email.')
				print("'This email is already in use! Try another email.'")
				return render(request,'register.html',{'message2':"This email is already in use! Try another email."})
		else:
			if password1==password2:
			    regis = User.objects.create_user(username=username,email=email,password=password1,phone=phone)
			    regis.save()
			    print("user created")
			else:
				# messages.info(request, 'Password is not match!')
				print("Password is not match!")
				return render(request,'register.html',{'message3':"Password is not match"})
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
			#messages.success(request, f" Hello {username}, You Are Successfully Logged In")
			print("You Are Successfully Logged In")
			return render(request,"success.html")
		else:
			if not User.objects.filter(username=username).exists():
				#messages.error(request, "Username Doesn't Exist")
				print("Username Doesn't Exist")
			else:
				#messages.info(request, "Incorrect Password")
				print("Incorrect Password")
			return redirect('login')
	else:
		return render(request,'login.html')

def logout(request):
	auth.logout(request)
	return redirect('/')

def review(request):
	if "book" in request.POST:
		origin_book = request.POST.get('origin_book')
		destination_book = request.POST.get('destination_book')
		flightnumber_book = request.POST.get('flightnumber_book')
		airline_book = request.POST.get('airline_book')
		depart_date_book = request.POST.get('depart_date_book')
		depart_time_book = request.POST.get('depart_time_book')
		return_date_book = request.POST.get('return_date_book')
		return_time_book = request.POST.get('return_time_book')
		amount_book = request.POST.get('amount_book')
		seat_class_book = request.POST.get('seat_class_book')
		if (return_date_book and return_time_book) != None:
			booking_review = {
				'origin_book':origin_book,
				'destination_book':destination_book,
				'flightnumber_book':flightnumber_book,
				'depart_date_book':depart_date_book,
				'depart_time_book':depart_time_book,
				'return_date_book':return_date_book,
				'return_time_book':return_time_book,
				'amount_book':amount_book,
				'seat_class_book':seat_class_book
			}
		else:
			booking_review = {
				'origin_book':origin_book,
				'destination_book':destination_book,
				'flightnumber_book':flightnumber_book,
				'depart_date_book':depart_date_book,
				'depart_time_book':depart_time_book,
				'amount_book':amount_book,
				'seat_class_book':seat_class_book
			}
		print("Recieve value",booking_review)
		return render(request,"review.html",booking_review)
	return render(request,"review.html")

        