from django.shortcuts import render

from article.models import Book

def book(request):
    '''
    Render the article page
    '''
    books = Book.objects.all()
    itemArray = []
    for book in books:
        items = [book]
        itemArray.append(items)
    context = {'itemArray':itemArray}
    return render(request, 'book/book.html',context)