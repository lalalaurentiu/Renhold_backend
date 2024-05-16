from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    A custom user manager for creating and managing user instances.
    """

    def create_user(self, email, **extra_fields):
        """
        Creates and saves a new user instance with the given email and extra fields.

        Args:
            email (str): The email address of the user.
            **extra_fields: Additional fields to be set for the user.

        Returns:
            User: The created user instance.
        
        Raises:
            ValueError: If the email field is not provided.
        """
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, **extra_fields):
        """
        Creates and saves a new superuser instance with the given email and extra fields.

        Args:
            email (str): The email address of the superuser.
            **extra_fields: Additional fields to be set for the superuser.

        Returns:
            User: The created superuser instance.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, **extra_fields)
