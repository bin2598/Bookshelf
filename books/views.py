from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Book
from django.urls import reverse_lazy

from .forms import BookUserCreationForm

class BooklistView(ListView):
    model = Book
    template_name = 'books/bookList.html'


class BookdetailView(DetailView):
    model = Book
    template_name = 'books/bookDetail.html'


class BookcreateView(CreateView):
    model = Book
    template_name = 'books/bookCreate.html'
    fields = '__all__'


class BookeditView(UpdateView):
    model = Book
    template_name = 'books/bookEdit.html'
    fields = '__all__'


class BookdeleteView(DeleteView):
    model = Book
    template_name = 'books/bookDelete.html'
    fields = '__all__'
    success_url = reverse_lazy('book-list')


class SignupView(CreateView):
    form_class = BookUserCreationForm
    success_url = reverse_lazy('book-list')
    template_name = 'registration/signup.html'
    
