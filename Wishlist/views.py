from django.shortcuts import render

from Browse.models import Book


def wishlist(request):
    args = {}
    books = Book.objects.all()
    print("Hello World")

    args['books'] = books
    print(args)

    return render(request, "wishlist.html", args)
