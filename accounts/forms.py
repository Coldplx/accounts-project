from django import forms
from django.contrib.auth.forms import UserCreationForm


class signupForm(UserCreationForm):
    template_name = 'accounts/form.html'
    email = forms.EmailField(max_length=100, required=True)

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'email', 'password1', 'password2']