from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Group
from .models import Menu

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=25, required=True)
    last_name = forms.CharField(max_length=25, required=True)
    #CHOICES = [(str(gr), gr) for gr in Group.objects.all()]
    #groups = forms.ChoiceField(choices=CHOICES, required=True)

    class Meta:
        model = User
        fields = ["username","email", "first_name", "last_name", "password1", "password2", "groups"]

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
    
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': '',
        'id': 'hi',
    }))

class PostForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ["food", "date"]