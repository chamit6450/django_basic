from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.all_books, name='all_books'),
    # path('books/search/', views.search_book, name = 'search_books'),
    path('books/<int:book_id>/', views.book_details, name='book_details'),
    # path('books/category/<str:category>/', views.category, name='category'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
]