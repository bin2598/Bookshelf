from django.contrib import admin
from .models import Book,BookUser
from django.contrib.auth.admin import UserAdmin

from .forms import BookUserChangeForm,BookUserCreationForm

class BookUserAdmin(UserAdmin):
    add_form = BookUserCreationForm
    form = BookUserChangeForm
    model = BookUser
    list_display = ['email', 'is_staff', 'first_name']


admin.site.register(Book)
admin.site.register(BookUser, BookUserAdmin)