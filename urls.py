"""Defines URL patterns for crazy_book_club."""

from django.urls import path
from . import views

app_name =  'crazy_books_clubs'

urlpatterns = [
    # Home page
    path('', views.index, name = 'index')
]