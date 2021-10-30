from django.contrib.auth.models import User, auth
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 

# Create your views here.
def index(request):
    return render(request,'index.html')

def success(request):
	return render(request,'success.html')

def register_request(request):
	if request.method=='POST':
		username = request.POST['username']
		firstname = request.POST['fname']
		lastname = request.POST['lname']
		email = request.POST['email_id']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		if password1==password2:
			x = User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password1)
			x.save()
			print("user created")
			return redirect('/')
		else:
			messages.info(request, 'Password is not match!') 
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
			if not User.objects.filter(username=username).exists():
				messages.error(request, "Username Doesn't Exist")
			else:
				messages.info(request, "Incorrect Password")
			return redirect('/')
	else:
		return render(request,'login.html')

def logout(request):
	auth.logout(request)
	return redirect('/')

        