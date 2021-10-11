from django.shortcuts import render
from about.models import AboutUS, OurTeam,OurCient
# Create your views here.

def home_view(request):
	about=AboutUS.objects.get(id=1)
	team=OurTeam.objects.all()
	client=OurCient.objects.all()

	context={
	'about':about,
	'team':team,
	'client':client
	}
	return render(request,'assets/about/about.html', context)
