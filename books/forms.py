from django import forms  
#from books.models import Book
from books.models import Book ,Program , OldQuestion, HandsOut# Faculty, Level, Semester, Program

'''class FacultyForm(forms.ModelForm):
	class Meta:
		model=Faculty
		fields = "__all__"  

class LevelForm(forms.ModelForm):
	class Meta:
		model=Level
		fields = "__all__"
class LevelEditForm(forms.ModelForm):
	class Meta:
		model=Level
		fields="__all__"
'''
class BookForm(forms.ModelForm):
	class Meta:
		model=Book
		fields = "__all__"
		widgets={
		model.cover_pic:forms.ImageField(required=False)
		}
'''
class SemForm(forms.ModelForm):
	class Meta:
		model=Semester
		fields="__all__"

class ProgramForm(forms.ModelForm):
	class Meta:
		model=Program
		fields="__all__"
'''
class EditBookForm(forms.ModelForm):
	class Meta:
		model=Book
		fields="__all__"


class ProgramForm(forms.ModelForm):
	class Meta:
		model=Program
		fields="__all__"
		widgets={
		model.pic:forms.ImageField(required=False)
		}


class ProgramEditForm(forms.ModelForm):
	class Meta:
		model=Program
		fields="__all__"
		
#FOR HANDSOUT AND OLD QUESTION
class OldQuestionForm(forms.ModelForm):
	class Meta:
		model= OldQuestion
		fields="__all__"

class OldQuestionEditForm(forms.ModelForm):
	class Meta:
		model= OldQuestion
		fields="__all__"

class HandsOutForm(forms.ModelForm):
	class Meta:
		model=HandsOut
		fields="__all__"

class HandsOutEditForm(forms.ModelForm):
	class Meta:
		model=HandsOut
		fields="__all__"