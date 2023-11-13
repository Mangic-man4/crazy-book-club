from http.client import HTTPResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BookForm, ReviewForm
from .models import Book
from .models import Review
from django.http import Http404, HttpResponse
# Create your views here.

def index(request):
    return render(request, 'Book/index.html')

def Books(request):
    """Show all books.""" 
    if request.user.is_authenticated:
        books = Book.objects.filter(user=request.user).order_by('date_added')
        context = {'books': books}
        return render(request, 'Book/Books.html', context)
    else:
        return HttpResponse("Please log in to view this page.")


def Reviews(request):
    """Show all reviews."""
    reviews = Review.objects.order_by('date_added')
    context = {'reviews': reviews}
    return render(request, 'Book/Reviews.html', context)

def book(request, book_id):
    """Show a single book and all it's reviews"""
    book = get_object_or_404(Book, id=book_id)
    if book.user != request.user:
        raise Http404
    reviews = Review.objects.filter(book=book).order_by('-date_added')
    context = {'book': book, 'reviews': reviews}
    return render(request, 'Book/Book.html', context)

# View for adding a new book
@login_required
def new_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            user = request.user
            
            new_book = form.save(commit=False)
            new_book.user = user
            new_book.save()

            return redirect('crazy_books_clubs:book_detail', book_id=new_book.pk)
    else:
        form = BookForm()
    return render(request, 'Book/new_book.html', {'form': form})

# View for adding a new review
@login_required
def new_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.book = book
            new_review.save()
            return redirect('crazy_books_clubs:book_detail', book_id=book_id)
    else:
        form = ReviewForm()

    return render(request, 'Book/new_review.html', {'form': form, 'book': book})

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if book.user != request.user:
        raise Http404
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('crazy_books_clubs:book_detail', book_id=review.book.id)
    else:
        form = ReviewForm(instance=review)

    context = {'form': form, 'review': review}
    return render(request, 'Book/edit_review.html', context)