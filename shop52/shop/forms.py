from django import forms
from .models import Genre, Publisher, Author, Book, Customer, Order, Cart, Review


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'photo']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price', 'cover_image', 'is_available', 'genre', 'publisher', 'author']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'total_price', 'status', 'items']

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['book', 'quantity']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'customer', 'rating']



