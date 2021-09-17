from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from home.models import About_Us, Mission,Program, Message_from_Principal
# Create your views here.
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
	return render(request,'home/home.html', context)
