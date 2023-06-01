from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import signupForm
from django.contrib import auth
from django.contrib.auth.views import (LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView,
                                        PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView )
from django.contrib import messages

# Create your views here.
class login(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('home')

class logout(LogoutView):
    template_name = 'accounts/logged_out.html'

class password_change(PasswordChangeView):
    template_name = 'accounts/password_change_form.html'

class password_change_done(PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'

class password_reset(PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'

class password_reset_done(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'

class password_reset_confirm(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'

class password_reset_complete(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'

class signup(FormView):
    template_name = 'accounts/signup.html'
    form_class = signupForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user:
            auth.login(self.request, user)

        return super().form_valid(form)
