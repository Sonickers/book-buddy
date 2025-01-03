from django.contrib.auth.models import User
from django.db import models


from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    FORMAT_CHOICES = [
        ("Physical", "Physical"),
        ("Kindle", "Kindle"),
        ("Audiobook", "Audiobook"),
    ]
    title = models.CharField(max_length=255)
    cover_url = models.URLField(blank=True)
    format = models.CharField(max_length=50, choices=FORMAT_CHOICES)
    pages = models.IntegerField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)


class UserLibrary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="library")
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="user_libraries"
    )
    status = models.CharField(max_length=50, default="TBR")
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    user_rating = models.FloatField(null=True, blank=True)
    pages_read = models.IntegerField(default=0)


class ReadingSession(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="sessions")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sessions")
    date = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField()  # In minutes
    pages_read = models.IntegerField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)  # 1-5
