from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('first/', first_view, name='first_view'),
    path('company/', company_view, name='company_view'),
    path('main/', main_view, name='main_view'),
    path('items/', items_view, name='items_view'),
    path('cart/', cart_view, name='cart_view'),
    path('contact/', contact_view, name='contact_view'),
    path('search/', search_view, name='search_view'),
    path('tovar/', tovar_view, name='tovar_view'),
    path('categories/', categories_view, name='categories_view'),
   



    path('genres/', GenreListView.as_view(), name='genre_list'),
    path('genres/<int:pk>/', GenreDetailView.as_view(), name='genre_detail'),
    path('genres/create/', GenreCreateView.as_view(), name='genre_create'),
    path('genres/<int:pk>/update/', GenreUpdateView.as_view(), name='genre_update'),
    path('genres/<int:pk>/delete/', GenreDeleteView.as_view(), name='genre_delete'),
    
    
    path('publishers/', PublisherListView.as_view(), name='publisher_list'),
    path('publishers/<int:pk>/', PublisherDetailView.as_view(), name='publisher_detail'),
    path('publishers/create/', PublisherCreateView.as_view(), name='publisher_create'),
    path('publishers/<int:pk>/update/', PublisherUpdateView.as_view(), name='publisher_update'),
    path('publishers/<int:pk>/delete/', PublisherDeleteView.as_view(), name='publisher_delete'),
    
    
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('authors/create/', AuthorCreateView.as_view(), name='author_create'),
    path('authors/<int:pk>/update/', AuthorUpdateView.as_view(), name='author_update'),
    path('authors/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),
    
    
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/create/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    
  
    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customers/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customers/<int:pk>/update/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),
    
]   
