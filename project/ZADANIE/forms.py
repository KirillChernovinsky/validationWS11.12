from django import forms


class UserForm(forms.Form):
    name = forms.CharField(required=True, label='Введите имя', widget=forms.TextInput(attrs={'class':'myclass'}))
    email = forms.EmailField(required=False, label="Введите email")
    password = forms.CharField(label='Введите пароль',widget=forms.PasswordInput(attrs={'class':'password'}))
    # required_css_class = 'myclass'

