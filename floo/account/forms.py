from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import widgets
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
SEX_CHOICES = (('M', '남'), ('W', '여'))

AGE_CHOICES = (('5', '10대 이하'), ('10', '10대'), ('20', '20대'),
               ('30', '30대'), ('40', '40대'), ('50', '50대 이상'))


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'profile','sex', 'age', ]


widgets = {
    'sex': forms.Select(
        attrs={
            'class': 'form-control',
        }
    ),
    'age': forms.Select(
        attrs={
            'class': 'form-control',
        }
    ),
}
