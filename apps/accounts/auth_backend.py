# apps/accounts/auth_backend.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class EmailBackend(ModelBackend):
    """
    Custom authentication backend to authenticate users by email.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(self.user_model.USERNAME_FIELD)

        try:
            # Try to get the user by email
            user = get_user_model().objects.get(email=username)
        except get_user_model().DoesNotExist:
            return None

        # Check if the user is active and the password is correct
        if user.check_password(password):
            return user
        return None
