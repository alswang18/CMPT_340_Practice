from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    user_types = [
        ("doctor", "doctor"),
        ("patient", "patient"),
    ]
    username = None
    email = models.EmailField(_('email address'), unique=True)
    user_type = models.CharField(max_length=255, choices=user_types, default="doctor")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email