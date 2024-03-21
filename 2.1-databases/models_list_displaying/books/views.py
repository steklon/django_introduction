from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render

from books.converters import DateConverter
from books.models import Book


def books_home(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)


def books_view(request):
    template = 'books/books_list.html'
    books_list = Book.objects.all()
    date_object = DateConverter()
    books_date_list = [{"date": date_object.to_url(b.pub_date),
                        "name": b.name,
                        'author': b.author
                        } for b in books_list]
    # books_date_list = [date_con.to_url(b.pub_date) for b in books_list]
    print(books_date_list)

    path = request.path[1:-1]
    print(path)
    context = {'books': books_date_list}
    return render(request, template, context)


def books_date_view(request, pub_date):
    template = 'books/books_list_date.html'
    date_object = DateConverter()
    books_list = Book.objects.filter(pub_date=date_object.to_python(pub_date))
    # book_back = Book.objects.filter(pub_date__lt=date_object.to_python(pub_date)).values('pub_date').first()
    # print(book_back)
    # # books_date_list = [{"date": date_object.to_url(b.pub_date),
    # #                     "name": b.name,
    # #                     'author': b.author
    # #                     } for b in books_list]
    #
    paginator = Paginator(books_list, 1)
    page = paginator.get_page(pub_date)
    # print(page)
    context = {'books': books_list,
               'page': page
               }

    return render(request, template, context)
