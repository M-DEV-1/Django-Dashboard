from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from . models import studentrecord

from django.contrib.auth.models import User

from django.forms.widgets import PasswordInput, TextInput

from django import forms

# Register/Create User

class RegisterUser(UserCreationForm):
    
    class Meta:
        
        model = User
        fields = ['username', 'password1', 'password2']

# Login User

class LoginUser(AuthenticationForm):
     username = forms.CharField(widget=TextInput())
     password = forms.CharField(widget=PasswordInput())
     
# Create Record 

class CreateRecord(forms.ModelForm):
     class Meta:
        
        model = studentrecord
        fields = ['firstname', 'lastname', 'parentnumber', 'address']
        
# Update Record

class UpdateRecord(forms.ModelForm):
     class Meta:
        
        model = studentrecord
        fields = ['firstname', 'lastname', 'parentnumber', 'address']