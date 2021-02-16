from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import BookUser

class BookUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = BookUser
        # fields = UserCreationForm.Meta.fields + ('first_name', 'phone_no',)
        fields = ['first_name', 'phone_no', 'username',]



class BookUserChangeForm(UserChangeForm): 

    class Meta:
        model = BookUser
        fields = UserChangeForm.Meta.fields