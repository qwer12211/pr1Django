from django.shortcuts import render

def first_view(request):
    return render(request, 'first.html')

def contact_view(request):
    return render(request, 'contact.html')

def main_view(request):
    return render(request, 'main.html')

def items_view(request):
    return render(request, 'items.html')

def cart_view(request):
    return render(request, 'cart.html')