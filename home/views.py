from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from home.models import About_Us, Mission,Program, Message_from_Principal
# Create your views here.
from home.forms import ContactForm


def Home_page(request):
	aboutus=get_object_or_404(About_Us, id=1)
	mission=get_object_or_404(Mission, id=1)
	program=Program.objects.all()
	message=get_object_or_404(Message_from_Principal, id=1)
	context={

		'aboutus':aboutus ,
		'mission': mission,
		'program': program,
		'message': message

	}
	#return render(request,'home/home.html', context)
	return render(request,'assets/home/home.html', context)

def contact(request):
	form=ContactForm()
	if request.method=="POST":
		form=ContactForm(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request,messages.SUCCESS,"Message Sent Successfully")
			return redirect('contact')
		else:
			form=ContactForm()
			messages.add_message(request,messages.SUCCESS,"Sorry!. We cannot send message. Please fill form as per requirement")
			return redirect('contact')
	
	context={
		'form':form
	}
	#return render(request, 'home/contact.html',context)
	return render(request, 'assets/home/contact.html',context)