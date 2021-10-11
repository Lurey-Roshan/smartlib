from django.contrib import admin

# Register your models here.
from books.models import   Book #,Level, Program, Semester,Faculty

#admin.site.register(Level)
#admin.site.register(Faculty)
#admin.site.register(Program)
#admin.site.register(Semester)
admin.site.register(Book)


