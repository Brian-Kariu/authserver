from datetime import timezone
from typing import Any
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
import uuid
from .managers import AuthUserManager
from django.core.mail import EmailMessage
from django.utils.translation import gettext_lazy as _

class AuthUser(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    permissions = models.TextField(blank=True)
    organisation = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['guid']

    objects = AuthUserManager()

    def __str__(self) -> str:
        """Represent a user using their email."""
        return self.email
    
    def email_user(self, subject: str, message: str, from_email: str = None, **kwargs: Any):
        """Send an email to this user."""
        email = EmailMessage(subject, message, from_email, recipient_list)
        email.send()

    class Meta:
        """User model options."""

        ordering = ("-updated", "-created")

