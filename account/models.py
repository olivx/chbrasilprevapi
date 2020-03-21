import os
from os.path import splitext
from uuid import uuid4

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.mail import send_mail
from django.db import models
from django.dispatch import receiver


def image_upload_to(instance, filename):
    _, filename_ext = splitext(filename)
    return f"avatar/foto/{instance.pk}/{uuid4()}.{filename_ext}"



class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        """ create aregular user """
        extra_fields.setdefault("is_active", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        """ create super user """
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, is_admin=True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """ Custom user model  """

    email = models.EmailField(unique=True, verbose_name="Email")
    nome = models.CharField("nome", max_length=30, blank=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    avatar = models.ImageField("Foto", null=True, blank=True, upload_to=image_upload_to)
    rua = models.CharField("rua", max_length=250, blank=True)
    cidade = models.CharField("cidade", max_length=250, blank=True)
    bairro = models.CharField("bairro", max_length=250, blank=True)
    estado = models.CharField("estado", max_length=250, blank=True)
    cep = models.CharField("cep", max_length=10, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Cliente"

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return self.get_full_name()

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Sends an email to this User."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
