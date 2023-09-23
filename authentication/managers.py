from django.contrib.auth.models import BaseUserManager
from django.db import models

class AuthUserManager(BaseUserManager):
    """A custom user manager."""

    def create_user(
        self,
        email=None,
        password=None,
        **extra_fields,
    ):
        """Create and save a User with the given email, password."""
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        user.email_user(subject="Account Successfully created!", message="Your account has been created", from_email=email)
        return user

    def create_superuser(
        self,
        email=None,
        password=None,
        **extra_fields,
    ):
        """Create and save a User with the given email, DOB and password."""
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        user = self.create_user(
            email=email,
            password=password,
            **extra_fields,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

    def get_queryset(self) -> models.QuerySet:
        """Limit to active users."""
        return super().get_queryset().filter(active=True)