from django import forms
from social_auth_1.models import Account


class Profile(forms.ModelForm):
    avatar = forms.ImageField(label='Аватар')

    first_name = forms.CharField(label='Имя')
    second_name = forms.CharField(label='Фамилия')
    third_name = forms.CharField(label='Отчество')

    about_you = forms.CharField(label='Обо мне')

    class Meta:
        model = Account
        fields = ['avatar', 'first_name', 'second_name', 'third_name',
                  'about_you']
