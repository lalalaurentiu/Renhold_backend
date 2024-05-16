from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import LoginOrRegister, Token

urlpatterns = [
    path("token/", Token.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("login/", LoginOrRegister.as_view(), name="login"),
]

"""
URL patterns for user-related endpoints.

- `/token/`: Endpoint for obtaining a JSON Web Token (JWT) pair.
- `/token/refresh/`: Endpoint for refreshing a JWT.
- `/login/`: Endpoint for user login or registration.

These URL patterns are used for handling user authentication and authorization in the Renhold project's backend.
"""
