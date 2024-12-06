from django.urls import path
from authcart import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.handlelogin, name="login"),
    path('logout/', views.handlelogout, name="logout"),
    path('password-reset-email/', views.RequestResetEmailView.as_view(), name='request-reset-email'),
    path('set-new-password/<uid64>/<token>', views.SetNewPasswordView.as_view(), name='set-new-password'),
    path('request-reset-email/', views.RequestResetEmailView.as_view(), name='request_reset_email'),
]
