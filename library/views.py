from django.shortcuts import render

# Create your views here.
from .models import Book


def main_page(request):
    if request.user.is_authenticated:
        books = Book.objects.filter(user=request.user)
        stats = {
            "total_books": books.count(),
            "books_read": books.filter(status="Read").count(),
            "tbr_books": books.filter(status="TBR").count(),
        }
        return render(
            request, "library/main_page.html", {"books": books, "stats": stats}
        )
    return render(request, "library/main_page.html")
