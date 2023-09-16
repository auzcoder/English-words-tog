from django.db import models
from django.utils import timezone
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models.signals import pre_save
from django.dispatch import receiver
import random



def generate_unique_user_id():
    while True:
        user_id = str(random.randint(10001, 99999))
        if not CustomUser.objects.filter(user_id=user_id).exists():
            break
    return user_id

@receiver(pre_save, sender=CustomUserManager)
def generate_user_id(sender, instance, **kwargs):
    if not instance.user_id:
        instance.user_id = generate_unique_user_id()

class Users(AbstractBaseUser, PermissionsMixin):
    user_id = models.IntegerField(_('User ID'), max_length=6, blank=True, null=True, unique=True, default=generate_unique_user_id)
    email = models.EmailField(_('Email'), unique=True, blank=True, null=True)
    



