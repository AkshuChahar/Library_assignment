from django.contrib import admin
from .models import  Book, BookInstance, Student

# Register your models here.

# admin.site.register(Book)
# admin.site.register(BookInstance)

class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'author', 'isbn')
    fields = ['book_name', 'author', 'isbn']

admin.site.register(Book, BookAdmin)

class BookInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'issued', 'due_date', 'id', 'borrower')
    fields = ['id', 'book', 'issued', 'due_date', 'borrower']

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mobile', 'address', 'joined_on')
    fields = ['first_name', 'last_name', 'mobile', 'address', 'joined_on']

admin.site.register(Student, StudentAdmin)
