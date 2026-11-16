from django.http import HttpResponse
from django.shortcuts import render
from books.models import Category, Book

def home(request):
    qs = Category.objects.all()
    context = {'object_list': qs}
    return render(request, 'books/categories.html', context)

def index(request):
    return render(request, 'index.html')
