from django import forms 

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=30,widget=forms.EmailInput(attrs={"class":"login-email"}))

    password = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={"class":"login-password"}))