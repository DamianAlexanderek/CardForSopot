from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

<<<<<<< HEAD

=======
>>>>>>> 90676be8fbcdc6ef98118a5f877f7437ae6d7610
urlpatterns = [
    # Widoki logowania.
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
<<<<<<< HEAD
=======
    path('partners/', views.partners, name='partners'),
>>>>>>> 90676be8fbcdc6ef98118a5f877f7437ae6d7610

    # Adresy URL przeznaczone do obsługi zmiany hasła.
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # Adresy URL przeznaczone do obsługi procedury zerowania hasła.
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Adresy URL przeznaczone do obsługi strony.

]
