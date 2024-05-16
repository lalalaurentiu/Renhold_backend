from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from django.db import models

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Represents a custom user in the system.

    Attributes:
        email (str): The email address of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        is_active (bool): Indicates whether the user is active or not.
        is_staff (bool): Indicates whether the user is a staff member or not.
        date_joined (datetime): The date and time when the user joined.

    Methods:
        __str__(): Returns a string representation of the user.

    """

    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
