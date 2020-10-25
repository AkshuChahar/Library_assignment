from django import forms
from catalog.models import Book, Student, BookInstance

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('book_name', 'author', 'isbn')

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'mobile', 'address', 'joined_on')


class IssueBookForm(forms.ModelForm):
    class Meta:
        model=BookInstance
        fields = ('id', 'book', 'issued', 'due_date', 'borrower')
