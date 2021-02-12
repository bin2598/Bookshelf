from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Book
from django.urls import reverse_lazy

class BooklistView(ListView):
    model = Book
    template_name = 'bookList.html'


class BookdetailView(DetailView):
    model = Book
    template_name = 'bookDetail.html'


class BookcreateView(CreateView):
    model = Book
    template_name = 'bookCreate.html'
    fields = '__all__'


class BookeditView(UpdateView):
    model = Book
    template_name = 'bookEdit.html'
    fields = '__all__'


class BookdeleteView(DeleteView):
    model = Book
    template_name = 'bookDelete.html'
    fields = '__all__'
    success_url = reverse_lazy('book-list')
