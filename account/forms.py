from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
    password = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('Username or password is wrong')
        return super(LoginForm, self).clean()


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label='Username')
    password = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, label='Re-type password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise forms.ValidationError('Passwords arent matched')
        return password2
