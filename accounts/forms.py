from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomerSignupForm(UserCreationForm):

    full_name = forms.CharField(max_length=255)

    email = forms.EmailField()

    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = CustomUser

        fields = (
            'full_name',
            'email',
            'phone_number',
            'password1',
            'password2',
        )

    def save(self, commit=True):

        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']

        user.full_name = self.cleaned_data['full_name']

        user.phone_number = self.cleaned_data['phone_number']

        user.role = 'CUSTOMER'

        if commit:
            user.save()

        return user

from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):

    username = forms.EmailField(
        label='Email'
    )