from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .models import Book, BookInstance, Student
from .forms import BookForm, StudentForm, IssueBookForm

# Create your views here.

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_students = Student.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances, 'num_students':num_students},
    )
    
class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book

class StudentListView(generic.ListView):
    model = Student

class StudentDetailView(generic.DetailView):
    model = Student

class LoanedBookByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.all().order_by('due_date')
    

def add_books(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
        else:
            return render(request, 'catalog/addbook.html', {"form":form}, status=400)
    else:
        form = BookForm()
        return render(request, 'catalog/addbook.html', {"form":form}, status=200)

def update_books(request, pk):
    obj = Book.objects.get(pk=pk)
    form = BookForm(instance=obj)
    if request.method == 'POST':
        form = BookForm(data=request.POST, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('books')
    return render(request, 'catalog/updatebook.html', {"form":form}, status=400)

def delete_books(request, pk):
    obj = get_object_or_404(Book, pk=pk)
    obj.delete()
    return redirect('books')

def add_students(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student')
        else:
            return render(request, 'catalog/addstudent.html', {"form":form}, status=400)
    else:
        form = StudentForm()
        return render(request, 'catalog/addstudent.html', {"form":form}, status=200)

def update_student(request, pk):
    obj = Student.objects.get(pk=pk)
    form = StudentForm(instance=obj)
    if request.method == 'POST':
        form = StudentForm(data=request.POST, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('student')
    return render(request, 'catalog/updatestudent.html', {"form":form}, status=400)


def delete_student(request, pk):
    obj = get_object_or_404(Student, pk=pk)
    obj.delete()
    return redirect('student')

def issue_book(request):
    if request.method == 'POST':
        form = IssueBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('issued')
        else:
            return render(request, 'catalog/issuebook.html', {"form":form}, status=400)
    else:
        form = IssueBookForm()
        return render(request, 'catalog/issuebook.html', {"form":form}, status=200)

def return_book(request, pk):
    obj = get_object_or_404(BookInstance, pk=pk)
    obj.delete()
    return redirect('issued')
