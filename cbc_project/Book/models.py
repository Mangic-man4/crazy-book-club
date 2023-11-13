from django.db import models
from django.contrib.auth.models import User


# Create your models here

class Book(models.Model):
    """
    Model representing a book.
    """
    name = models.CharField(max_length=255)
    authors = models.JSONField(default=list)  # JSONField for a list of names
    year_published = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    # Date fields for tracking when the book was added and modified
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String representation of the book model.
        """
        return self.name
    
class Review(models.Model):
    """
    Model representing a review for a book.
    """
    my_review = models.TextField()
    stars = models.IntegerField()
    unfinished = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # ForeignKey to the Book model

    def __str__(self):
        """
        String representation of the review.
        """
        return f"Review for {self.book.name} by {self.book.authors[0]}"
    
    class Meta:
        """
        Additional metadata for the Review model.
        """
        verbose_name_plural = "Reviews"