from django.shortcuts import render, redirect
from validate_email import validate_email
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from member.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.
from member.forms import UserEditForm

def register(request):
	if request.method=="POST":
		context={
		'has_error':False,
		'data':request.POST
		}
		email=request.POST.get('email')
		username=request.POST.get('username')
		password=request.POST.get('password')
		password2=request.POST.get('password2')
		
		print(email)
		print(username)
		print(password)

		if len(password)<6:
			messages.add_message(request,messages.ERROR, "Password should be at least 6 character")
			context['has_error']=True
		if password != password2:
			messages.add_message(request,messages.ERROR, "Password Mismatched")
			context['has_error']=True


		if not validate_email(email):
			messages.add_message(request,messages.ERROR, 'Enter a valid email address')
			context['has_error']=True

		if not username:
			messages.add_message(request,messages.ERROR, 'Username Required')
			context['has_error']=True

		if User.objects.filter(username=username).exists():
			messages.add_message(request, messages.ERROR,"Username is taken, Choose another username")
			context['has_error']=True

		if User.objects.filter(email=email).exists():
			messages.add_message(request, messages.ERROR,"Email is already taken, try with another")
			context['has_error']=True

		if context['has_error']:
			return render(request,'member/newregister.html',context)
		else:
			user=User.objects.create_user(username=username,email=email)
			user.set_password(password)
			user.save()
			messages.add_message(request,messages.SUCCESS,"Account created successfully, You can login now")
		return redirect('login')

	return render(request,'member/newregister.html')

@login_required(login_url='/member/login')
def logout_user(request):
	logout(request)
	messages.add_message(request,messages.SUCCESS,"Successfully Logout ")
	return redirect('login')


def login_user(request):
	if request.method=="POST":
		context={
			'data':request.POST
		}
		username=request.POST.get('username')
		password=request.POST.get('password')
		print(username)
		print(password)
		user=authenticate(request,username=username, password=password)


		if not user:
			messages.add_message(request,messages.ERROR,"Invalid Credintials. Please Review your Username and Password")
			return render(request,'member/newlogin.html', context)
		login(request,user)
		messages.add_message(request,messages.SUCCESS,f"Welcome {user.username}  ")
		return redirect(reverse('home'))
	return render(request,'member/newlogin.html')


@login_required(login_url='/member/login')
def users(request):
	users=User.objects.all()
	context={
		'users':users
	}
	return render(request,'member/user.html', context)


@login_required(login_url='/member/login')
def user_delete(request, id):
	user=User.objects.get(pk=id)
	print(user)
	user.delete()
	messages.add_message(request, messages.SUCCESS, "User Deleted Successfully")
	return render(request, 'member/user.html')


@login_required(login_url='/member/login')
def edit_user(request, id):
	mem=get_object_or_404(User, pk=id)
	form=UserEditForm(instance=mem)
	if request.method=="POST":
		form=UserEditForm(request.POST, instance=mem)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, "User Updated Successfully")
			#return redirect('user_detail')
			return HttpResponseRedirect(reverse("user_detail", kwargs={'id':mem.pk}))
		else:
			print(false)
			messages.add_message(request, messages.ERROR, "User Cannot updated")
			form=UserEditForm(instance=mem)
			
	context={
		'form':form,
		'mem':mem
	}
	return render(request,'member/edit_user.html', context)
	#mem for user
def user_detail(request, id):
	mem=get_object_or_404(User, pk=id)
	context={
		'mem':mem
	}
	return render(request,'member/userdetail.html',context)