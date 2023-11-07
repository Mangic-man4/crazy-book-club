"""Defines URL patterns for crazy_book_club."""

from django.urls import path
from . import views

app_name =  'crazy_books_clubs'

urlpatterns = [
    # Home page
    path('', views.index, name = 'index'),
    # Book list page
    path('Books', views.Books, name = 'Books'),
    # Reviews list page
    path('Reviews', views.Reviews, name = 'Reviews'),
    # Detail page for a single book
    path('book_detail/<int:book_id>/', views.book, name = 'book_detail'),
    # URL for new_book page
    path('new_book/', views.new_book, name='new_book'),
    # URL for new_review page
    path('new_review/<int:book_id>/', views.new_review, name='new_review'),
    # Edit review
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review')
]