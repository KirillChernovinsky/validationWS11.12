from django import forms


class UserForm(forms.Form):
    #widget=forms.TextInput(attrs={'class':'myclass'}
    name = forms.CharField(required=True, label='Имя')
    age = forms.IntegerField(required=False)
    email = forms.EmailField(required=False)
    required_css_class = 'myclass'

