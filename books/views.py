from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from books. models import   Level,Faculty ,Book,Program,Semester
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from books.forms import FacultyForm, LevelForm, BookForm, SemForm, ProgramForm, EditBookForm,LevelEditForm,SearchForm

from PyPDF2 import PdfFileReader
from django.http import FileResponse, Http404
import os
from django.conf import settings
# Create your views here.
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

#new 
from django.views import View
from django.views.generic import ListView
from books.filters import BookFilter




def home(request ):
	return render(request, 'home.html')
#for book

def courses(request):
	program=Program.objects.all()
	faculty=Faculty.objects.all()
	level=Level.objects.all()
	context={
		'program':program,
		'faculty':faculty,
		'level':level
	}
	#return render(request, 'books/course.html', context)
	return render(request, 'assets/book/course.html',context)
	
class BookListView(ListView):
	model=Book
	template_name='assets/book/lib.html'
	#template_name='books/book.html'

	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		context['filter']=BookFilter(self.request.GET ,queryset=self.get_queryset())
		return context



@login_required(login_url='/member/login')	
def book_detail(request, id):
	book=get_object_or_404(Book, pk=id)
	context={
		'book':book
	}
	#return render(request,'books/book_detail.html', context)
	return render(request,'assets/book/book_detail.html', context)

@login_required(login_url='/member/login')
def create_book(request):
	form=BookForm()
	if request.method== "POST":
		form=BookForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.add_message(request,messages.SUCCESS,"Book Added Successfully")
			return redirect('index')
		else:
			messages.add_message(request,messages.ERROR,"Please Fill the form well and make sure the file has .pdf extension")
			form=BookForm()
	context={
		'form':form
	}
	
			
	

	#return render(request, 'books/create_book.html',context)
	return render(request, 'assets/book/createbook.html',context)


@login_required(login_url='/member/login')
def delete_book(request, id):
	b=get_object_or_404(Book, pk=id)
	b.delete()
	messages.add_message(request, messages.SUCCESS,"Deleted Successfully")
	return redirect('index')


@login_required(login_url='/member/login')
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

	#return render(request,'books/edit_book.html', context)
	return render(request,'assets/book/edit_book.html', context)


@login_required(login_url='/member/login')
def level_index(request):
	level=Level.objects.all()
	context={
		'level':level
	}
	return render(request,'books/level_index.html', context)

@login_required(login_url='/member/login')
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

@login_required(login_url='/member/login')
def create_level(request):
	form=LevelForm()
	if request.method=="POST":
		form=LevelForm(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request,messages.SUCCESS,"Level Created Successfully")
			return redirect('course')
	context={
		'form': form

	}
	
	#return render(request,'books/create_level.html',context)
	return render(request,'assets/book/add_level.html',context)

@login_required(login_url='/member/login')
def create_faculty(request):
	form=FacultyForm()
	if request.method=="POST":
		form=FacultyForm(request.POST)

		if form.is_valid():
			form.save()
			messages.add_message(request,messages.SUCCESS,"Faculty Created Successfully")
			return redirect('course')
	context={
		'form': form
	}

	#return render(request,'books/create_faculty.html',context)
	return render(request,'assets/book/add_faculty.html',context)



@login_required(login_url='/member/login')
def create_program(request):
	form=ProgramForm()
	if request.method=="POST":
		form=ProgramForm(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request,messages.SUCCESS,"Program Created Successfully")
			return redirect('course')
	context={
		'form': form
	}
	#return render(request, 'books/create_program.html',context)
	return render(request, 'assets/book/add_program.html',context)

@login_required(login_url='/member/login')
def create_sem(request):
	form=SemForm()
	if request.method=="POST":
		form=SemForm(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request,messages.SUCCESS,"Program Created Successfully")
			return redirect('course')
	context={
		'form': form
	
	}
	#return render(request, 'books/create_sem.html',context)
	return render(request, 'assets/book/add_sem.html',context)



	

def view_image(request, id):
	book=Book.objects.get(pk=id)
	context={
		'book':book
	}
	return render(request,'books/view_image.html', context)
	
@login_required(login_url='/member/login')
def delete_level(request, id):
	level=get_object_or_404(Level, pk=id)
	level.delete()
	return redirect('course')

	
@login_required(login_url='/member/login')
def delete_sem(request, id):
	sem=get_object_or_404(Semester, pk=id)
	sem.delete()
	return redirect('course')


@login_required(login_url='/member/login')
def delete_program(request, id):
	program=get_object_or_404(Program, pk=id)
	program.delete()
	return redirect('course')



@login_required(login_url='/member/login')
def delete_faculty(request, id):
	faculty=get_object_or_404(Faculty, pk=id)
	faculty.delete()
	return redirect('course')



def view_pdf(request, id):
	book=Book.objects.get(pk=id).file.url
	print(book)
	with open(book, 'rb') as pdf:
		response = HttpResponse(pdf.read(),content_type='application/pdf')
		response['Content-Disposition'] = 'filename=book.book_name.pdf'
		return response