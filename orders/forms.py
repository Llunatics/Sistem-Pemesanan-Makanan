from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class Registration(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control form-control-sm rounded-0', 'placeholder':"ismet"})
        self.fields['password1'].widget.attrs.update({'class':'form-control form-control-sm rounded-0', 'placeholder':"*******"})
        self.fields['password2'].widget.attrs.update({'class':'form-control form-control-sm rounded-0', 'placeholder':"*******"})

class Login(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control form-control-sm rounded-0', 'placeholder':"gathan"})
        self.fields['password'].widget.attrs.update({'class':'form-control form-control-sm rounded-0', 'placeholder':"*******"})