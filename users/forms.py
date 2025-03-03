from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from catalog.forms import MixinProduct

from .models import ModelUser


class MixinValidPhoneNumber:
    """Миксин для проверки валидности номера телефона"""

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("Номер телефона должен состоять только из цифр")
        return phone_number


class UserAuthenticationForm(MixinProduct, AuthenticationForm):
    """Форма авторизации"""

    pass


class CustomUserCreationForm(MixinProduct, UserCreationForm, MixinValidPhoneNumber):
    """Форма регистрации профиля"""

    phone_number = forms.CharField(max_length=15, required=False, label="Номер телефона")
    username = forms.CharField(max_length=100, required=True)
    avatar = forms.ImageField(required=False, label="Аватар")

    class Meta:
        model = ModelUser
        fields = (
            "email",
            "username",
            "phone_number",
            "avatar",
            "password1",
            "password2",
        )


class ProfileUserForm(MixinProduct, forms.ModelForm, MixinValidPhoneNumber):
    """Форма профиля"""

    class Meta:
        model = ModelUser
        fields = ("last_name", "first_name", "username", "phone_number", "avatar", "country")
