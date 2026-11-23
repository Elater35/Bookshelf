from django.urls import path
from books.views import *

urlpatterns = [
    path('', index, name='index'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
]