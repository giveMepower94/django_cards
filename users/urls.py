from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


app_name = 'users'  # Пространство имен для приложения


urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),
    path('signup/', views.RegisterUser.as_view(), name='signup'),
    path('register_done/', views.RegisterDone.as_view(), name='register_done'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
    path('password_change/', views.UserPasswordChange.as_view(), name='password_change'),
    path('password_change_done/', views.UserPasswordChangeDone.as_view(), name='password_change_done'),
    path('profile_cards/', views.UserCardsView.as_view(), name='profile_cards'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset_form.html',
             email_template_name='users/password_reset_email.html',
             success_url = reverse_lazy('password_reset_done')),
         name='password_reset'),
    path('password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name = 'users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset_done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name = 'users/password_reset_complete.html'),
         name='password_reset_complete'),
]