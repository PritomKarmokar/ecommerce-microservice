from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from users.views import (
    LoginView,
    SignUpView,
    LogoutView,
    ProfileView
)


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("profile/", ProfileView.as_view(), name="profile_view"), # endpoint for 'get' and 'update'
]