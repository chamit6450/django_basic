from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

BOOKS = [
    {"id":1, 'title': 'The Great Django', 'author':'Django', 'category': 'fiction'},
    {"id":2, 'title': 'The Great Django1', 'author':'Django1', 'category': 'fiction1'},
    {"id":3, 'title': 'The Great Django2', 'author':'Django2', 'category': 'fiction2'},
    {"id":4, 'title': 'The Great Django3', 'author':'Django3', 'category': 'fiction3'},
]

def home(request):
    return HttpResponse("<h1>Welcome to libraray management system</h1>")

def about(request):
    return HttpResponse("<h1>about us</h1>")

def contact(request):
    return HttpResponse("<h1>contact us</h1>")

def all_books(request):
    return JsonResponse({"books":BOOKS})

def book_details(request, book_id):
    book=((book for book in BOOKS if book["id"] == book_id))
    # return HttpResponse("<h1>The details of books are: ID:{id} </h1>")
    return JsonResponse({'book':book} if book else {f'message':"book ID with {book_id} not found"})