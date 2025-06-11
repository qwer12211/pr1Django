from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import *


def first_view(request):
    return render(request, 'first.html')

def company_view(request):
    return render(request, 'company.html')

def main_view(request):
    return render(request, 'main.html')

def items_view(request):
    return render(request, 'items.html')

def cart_view(request):
    return render(request, 'cart.html')

def contact_view(request):
    return render(request, 'contact.html')

def search_view(request):
    return render(request, 'search.html')

def categories_view(request):
    return render(request, 'categories.html')


def tovar_view(request):
    return render(request, 'tovar.html')




class GenreListView(ListView):
    model = Genre
    template_name = 'shop/genre_list.html'
    context_object_name = 'genres'

class GenreDetailView(DetailView):
    model = Genre
    template_name = 'shop/genre_detail.html'
    context_object_name = 'genre'

class GenreCreateView(CreateView):
    model = Genre
    form_class = GenreForm
    template_name = 'shop/genre_form.html'
    success_url = reverse_lazy('genre_list')

class GenreUpdateView(UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = 'shop/genre_form.html'
    success_url = reverse_lazy('genre_list')

class GenreDeleteView(DeleteView):
    model = Genre
    template_name = 'shop/genre_confirm_delete.html'
    success_url = reverse_lazy('genre_list')



class PublisherListView(ListView):
    model = Publisher
    template_name = 'shop/publisher_list.html'
    context_object_name = 'publishers'

class PublisherDetailView(DetailView):
    model = Publisher
    template_name = 'shop/publisher_detail.html'
    context_object_name = 'publisher'

class PublisherCreateView(CreateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'shop/publisher_form.html'
    success_url = reverse_lazy('publisher_list')

class PublisherUpdateView(UpdateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'shop/publisher_form.html'
    success_url = reverse_lazy('publisher_list')

class PublisherDeleteView(DeleteView):
    model = Publisher
    template_name = 'shop/publisher_confirm_delete.html'
    success_url = reverse_lazy('publisher_list')


class AuthorListView(ListView):
    model = Author
    template_name = 'shop/author_list.html'
    context_object_name = 'authors'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'shop/author_detail.html'
    context_object_name = 'author'

class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'shop/author_form.html'
    success_url = reverse_lazy('author_list')

class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'shop/author_form.html'
    success_url = reverse_lazy('author_list')

class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'shop/author_confirm_delete.html'
    success_url = reverse_lazy('author_list')

# Book Views
class BookListView(ListView):
    model = Book
    template_name = 'shop/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'shop/book_detail.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'shop/book_form.html'
    success_url = reverse_lazy('book_list')

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'shop/book_form.html'
    success_url = reverse_lazy('book_list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'shop/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')

# Customer Views
class CustomerListView(ListView):
    model = Customer
    template_name = 'shop/customer_list.html'
    context_object_name = 'customers'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'shop/customer_detail.html'
    context_object_name = 'customer'

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'shop/customer_form.html'
    success_url = reverse_lazy('customer_list')

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'shop/customer_form.html'
    success_url = reverse_lazy('customer_list')

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'shop/customer_confirm_delete.html'
    success_url = reverse_lazy('customer_list')