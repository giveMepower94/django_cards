from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm, UserPasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from  django.views.generic import CreateView, TemplateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from cards.models import Card
# Create your views here.

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        next_url = self.request.POST.get('next', '').strip()
        if next_url:
            return next_url
        return reverse_lazy('catalog')


class LogoutUser(LogoutView):
    next_page = reverse_lazy('users:login')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('users:register_done')


class RegisterDone(TemplateView):
    template_name = 'users/register_done.html'
    extra_context = {'title': 'Регистрация завершена!'}


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {'title': 'Профиль пользователя'}

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'users/password_change_form.html'
    success_url = reverse_lazy('users:password_change_done')


class UserPasswordChangeDone(TemplateView):
    template_name = 'users/password_change_done.html'
    extra_context = {'title': 'Пароль изменен успешно'}


class UserCardsView(ListView):
    model = Card
    template_name = 'users/profile_cards.html'
    context_object_name = 'cards'

    def get_queryset(self):
        return Card.objects.filter(author=self.request.user).order_by('-upload_date')