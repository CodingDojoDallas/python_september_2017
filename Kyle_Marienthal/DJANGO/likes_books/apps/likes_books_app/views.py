from django.shortcuts import render, redirect, reverse

# Create your views here.
def index(request):
    return render(request, 'likes_books_app/index.html')
