from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Profile

class CustomUserCreationForm(UserCreationForm):

    email = forms.EmailField(required=True) # Email requied.

    def clean_email(self):
        """Checking to see if e-mail is in use."""
        if CustomUser.objects.filter(email=self.cleaned_data['email'].lower()).exists():

            raise forms.ValidationError("The given E-mail is already registered.")

        return self.cleaned_data['email']

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email'].lower()
        if commit:
            user.save()
        return user


    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'age',)

# Form used to update user info.
class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUser
        fields = ('username',)

# Form used to update profile info.
class ProfileUpdateForm(UserChangeForm):
    password = None

    class Meta:
        model = Profile
        fields = ['image', 'bio']