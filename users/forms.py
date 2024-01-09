from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='Email',
        required=True,
    )
    # username = forms.CharField(
    #     label='Имя пользователя',
    #     required=True,
    #     help_text='Обязательное поле. Нельзя вводить символы: @, /, _',
    #     widget=forms.TextInput(attrs={'placeholder': 'Введите имя'})
    # )
    # password1 = forms.CharField(
    #     label='Пароль',
    #     required=True,
    #     widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'})
    # )
    # password2 = forms.CharField(
    #     label='Подтвердите пароль',
    #     required=False,
    #     widget=forms.PasswordInput(attrs={'placeholder': 'Повторно введите пароль'})
    # )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        del self.fields['password2']


class UserUpdateForm(forms.ModelForm):
    # email = forms.EmailField(
    #     label='Введите Email',
    #     required=True
    # )
    # username = forms.CharField(
    #     label='Введите логин',
    #     required=True,
    #     help_text='Нельзя вводить символы: @, /, _',
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    # )
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label='Загрузить фото',
        required=False,
        widget=forms.FileInput
    )

    class Meta:
        model = Profile
        fields = ['img']
