from django.urls import path
from restProject.views import lista_alumnos, lista_asistencia, usuario_login, cambiar_contrasena, crear_usuario
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('lista_asistencia/', lista_asistencia, name='lista de asistencia'),
    path('lista_alumnos/', lista_alumnos, name='lista de choros'),
    path('login', usuario_login, name='Login'),
    path('recuperar', cambiar_contrasena, name='Login'),
    path('crear', crear_usuario, name='Login')
    # path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    # path('reset_password/', auth_views.PasswordResetView.as_view(), name = 'reset_password'),
    # path('reset_password_sent/', auth_views.PasswordResetView.as_view(), name = 'password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    # path('reset_password_complete/', auth_views.PasswordResetView.as_view(), name = 'password_reset_complete')



    
]