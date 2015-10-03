from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from mentor.models import UserProfile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
            user_profile = UserProfile(user=user)
            user_profile.save()
        return user
