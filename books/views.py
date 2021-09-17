from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from books. models import   Level,Faculty ,Book,Program,Semester
from django.http import HttpResponseRedirect
from django.urls import reverse

from books.forms import FacultyForm, LevelForm, BookForm, SemForm, ProgramForm, EditBookForm,LevelEditForm,SearchForm
# Create your views here.
#new 
from django.views import View
from django.views.generic import ListView
from books.filters import BookFilter


def home(request ):
	return render(request, 'home.html')
#for book
class BookListView(ListView):
	model=Book
	template_name='books/book.html'

	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		context['filter']=BookFilter(self.request.GET ,queryset=self.get_queryset())
		return context
	
def book_detail(request, id):
	book=get_object_or_404(Book, pk=id)
	return render(request,'books/book_detail.html', {'book':book})

def create_book(request):
	form=BookForm()
	if request.method== "POST":
		form=BookForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.add_message(request,messages.SUCCESS,"Book Added Successfully")
			return redirect('index')
		else:
			messages.add_message(request,messages.ERROR,"Please Fill the form well")
			form=BookForm(instance=form.data)
	context={
	'form': form
	
	}

	return render(request, 'books/create_book.html',context)

def delete_book(request, id):
	b=get_object_or_404(Book, pk=id)
	b.delete()
	messages.add_message(request, messages.SUCCESS,"Deleted Successfully")
	return redirect('index')


def edit_book(request, id):
	book=get_object_or_404(Book, pk=id)
	form=EditBookForm(instance=book)
	if request.method=="POST":
		form=EditBookForm(request.POST, instance=book)
		if form.is_valid():
			form.save()
			messages.add_message(request,messages.SUCCESS,"Updated Successfully")
			return HttpResponseRedirect(reverse("book_detail", kwargs={'id':book.pk}))
	context={
		'form':form,
		'book':book
	}

	return render(request,'books/edit_book.html', context)


def level_index(request):
	level=Level.objects.all()
	context={
		'level':level
	}
	return render(request,'books/level_index.html', context)

def edit_level(request, id):
	lvl=get_object_or_404(Level, pk=id)
	form=LevelEditForm(instance=lvl)
	if request.method=="POST":
		form=LevelEditForm(request.POST, instance=lvl)
		if form.is_valid():
			form.save()
			messages.add_message(request,messages.SUCCESS,"Updated Successfully")
			return redirect('level_index')

		else:
			form=LevelEditForm()
			messages.add_message(request,messages.ERROR,"Couldnot Update")
	context={
	'lvl':lvl,
	'form':form
	}
	return render(request,'books/level_edit.html', context)

def create_level(request):
	form=LevelForm()
	if request.method=="POST":
		form=LevelForm(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request,messages.SUCCESS,"Level Created Successfully")
			return redirect('level_index')
	context={
		'form': form

	}
	return render(request,'books/create_level.html',context)

def create_faculty(request):
	form=FacultyForm()
	if request.method=="POST":
		form=faculty(request.POST)

		if form.is_valid():
			form.save()
			messages.add_message(request,messages.SUCCESS,"Faculty Created Successfully")
			return redirect('index')
	context={
		'form': form
	}

	return render(request,'books/create_faculty.html',context)


def create_program(request):
	form=ProgramForm()
	if request.method=="POST":
		form=ProgramForm(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request,messages.SUCCESS,"Program Created Successfully")
			return redirect('index')
	context={
		'form': form
	}
	return render(request, 'books/create_program.html',context)

def create_sem(request):
	form=SemForm()
	if request.method=="POST":
		form=SemForm(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request,messages.SUCCESS,"Program Created Successfully")
			return redirect('index')
	context={
		'form': form
	
	}
	return render(request, 'books/create_sem.html',context)


