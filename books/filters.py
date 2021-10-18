import django_filters

from books.models import Book,OldQuestion, HandsOut

class BookFilter(django_filters.FilterSet):
	class Meta:
		model=Book
		fields=('level','faculty', 'program', 'sem', 'book_name','author','published_By')



class OldQuestionFilter(django_filters.FilterSet):
	class Meta:
		model=OldQuestion
		fields=('level','faculty', 'program', 'sem', 'subject', 'year')


class HandsOutFilter(django_filters.FilterSet):
	class Meta:
		model=HandsOut
		fields=('level','faculty','program','sem','subject','note_by')