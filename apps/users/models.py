from django.db import models
from django.contrib.auth.models import AbstractUser

# # Create your models here.
class User(AbstractUser):   
    phone = models.CharField(
        max_length=100,
        verbose_name="Телефонный номер",
        blank=True,null=True
        )
    profile_image = models.ImageField(
        upload_to="profile_image/",
        blank=True,null=True
    )
    locate = models.CharField(
        max_length=255,
        verbose_name="Адрес",
        blank=True,null=True
    )
    descriptions = models.TextField(
        verbose_name="Описание",
        blank=True,null=True
    )
    telegram = models.URLField(
        verbose_name="Facebook",
        blank=True,null=True
    )
    instagram = models.URLField(
        verbose_name="Instagram",
        blank=True,null=True
    )
    youtube = models.URLField(
        verbose_name="Youtube",
        blank=True,null=True
    )

    def __str__(self):
        return self.username