from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    total_books = books.count()
    return render(request, 'index.html', {'books': books, 'total_books': total_books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm()

    return render(request, 'books/add_book.html', {'form': form})
