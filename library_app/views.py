from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book
from .forms import BookForm

# Display all books
def index(request):
    books = Book.objects.all()
    return render(request, 'library_app/index.html', {'books': books})

# Add a book
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm()
    return render(request, 'library_app/add_book.html', {'form': form})

# Update a book
def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id) 
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm(instance=book)
    return render(request, 'library_app/update_book.html', {'form': form, 'book': book})

# Delete a book
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('index')

# Search books
def search_books(request):
    keyword = request.GET.get('keyword', '')
    books = Book.objects.filter(title__icontains=keyword) | Book.objects.filter(author__icontains=keyword)
    return render(request, 'library_app/index.html', {'books': books, 'keyword': keyword})