from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Book(models.Model):
    book_name = models.CharField('Book', max_length=200)
    author = models.CharField('Author', max_length=200)
    isbn = models.CharField('ISBN', max_length=13)

    def __str__(self):
        return self.book_name

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"

class BookInstance(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    issued = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey('Student', on_delete=models.CASCADE, null=True, blank=True)


    class Meta:
        ordering = ["issued", "due_date"]
        permissions = [("can_mark_issued", "Set book as issued"), ("can_mark_returned", "Set book as returned"),]


    def __str__(self):
        return self.book.book_name


    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"
    
class Student(models.Model):
    first_name = models.CharField('First Name', max_length=200)
    last_name = models.CharField('Last Name', max_length=200)
    mobile = models.CharField('Mobile', max_length=10)
    address = models.CharField('Address', max_length=400)
    joined_on = models.DateField()
    book_issued = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"
    
