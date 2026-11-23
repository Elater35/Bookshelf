from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from books.models import Category, Book

def home(request, pk=None):
    if pk:
        category = get_object_or_404(Category, id=pk)
        context = {'object': category}
        return render(request, 'books/category_detail.html', context)

    qs = Category.objects.all()
    context = {'object_list': qs}
    return render(request, 'books/categories.html', context)

def index(request):
    return render(request, 'index.html')


class CategoryListView(ListView):
    model = Category
    template_name = 'books/categories.html'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'books/category_detail.html'
