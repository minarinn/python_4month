from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField
from .models import CustomUser


class LoginWithCaptchaForm(AuthenticationForm):
    captcha = CaptchaField()


class CustomRegisterForm(UserCreationForm):
    resume = forms.FileField(required=False)

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'age',
            'gender',
            'education_level',
            'experience_years',
            'desired_position',
            'skills',
            'address',
            'resume',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(CustomRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        if commit:
            user.save()
        return user
