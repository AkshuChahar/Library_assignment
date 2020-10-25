from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),


    path('books/', views.BookListView.as_view(), name='books'),
    path('add_book/', views.add_books, name='add_book'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('update_book/<int:pk>', views.update_books, name='update_book'),
    path('delete_book/<int:pk>', views.delete_books, name='delete_book'),


    path('students/', views.StudentListView.as_view(), name='student'),
    path('add_student/', views.add_students, name='add_student'),
    path('students/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
    path('update_student/<int:pk>', views.update_student, name='update_student'),
    path('delete_student/<int:pk>', views.delete_student, name='delete_student'),


    path('issued/', views.LoanedBookByUserListView.as_view(), name='issued'),
    path('issue_book/', views.issue_book, name='issue_book'),
    path('return_book/<int:pk>', views.return_book, name='return_book'),
]
