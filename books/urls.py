from django.urls import path
from books.views import home, index

urlpatterns = [
    path('', index, name='index'),
    path('category/', home, name='category'),
]