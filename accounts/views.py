from django.shortcuts import render, get_object_or_404
from .forms import UserProfileForm,UserForm
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def register(request):
	registered = False
	if request.method == 'POST':
		# in here we can pass request.POST in form using with 'data' variable or without 'data' variable
		user_form = UserForm(data=request.POST)
		user_profile_form = UserProfileForm(request.POST)
		if user_form.is_valid() and user_profile_form.is_valid():
			user = user_form.save()
			user_profile = user_profile_form.save(commit=False)
			user_profile.user = user
			if 'address' in request.POST:
				address = request.POST['address']
			else:
				address = ''
			if 'phone' in request.POST:
				phone = request.POST['phone']
			else:
				return HttpResponse("Phone is required!")
			user_profile.address = address
			user_profile.phone = phone
			user_profile.save()
			registered = True
			return HttpResponseRedirect(reverse('homepage'))
		else:
			return HttpResponse(user_form.errors,user_profile_form.errors)
	else:
		user_form = UserForm()
		user_profile_form = UserProfileForm()
		context ={
			'user_profile_form':user_profile_form,
			'user_form':user_form,
			'registered':registered
		}
		return render(request,'accounts/register.html',context)

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		if username == None or password == None:
			return HttpResponse("Please provide both username and password")
		user = get_object_or_404(User.objects.filter(username=username,password=password))
		# user = authenticate(username=username,password=password)
		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('homepage'))
			else:
				return HttpResponse("Your account was inactive")
		else:
			return HttpResponse('invalid login details given')
	else:
		context={}
		return render(request,'accounts/user_login.html',context)

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('homepage'))
