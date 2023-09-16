from django.db import models
from django.utils import timezone
from users.managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models.signals import pre_save
from django.dispatch import receiver
import random



def generate_unique_user_id():
    while True:
        user_id = str(random.randint(10001, 99999))
        if not CustomUsers.objects.filter(user_id=user_id).exists():
            break
    return user_id

@receiver(pre_save, sender=CustomUserManager)
def generate_user_id(sender, instance, **kwargs):
    if not instance.user_id:
        instance.user_id = generate_unique_user_id()


# default = generate_unique_user_id
class CustomUsers(AbstractBaseUser, PermissionsMixin):
    user_id = models.IntegerField(_('User ID'), blank=False, null=False, unique=True, default=generate_unique_user_id)
    username = models.CharField(_('Username'), max_length=15, blank=False, null=False, unique=True)
    email = models.EmailField(_('Email'), unique=True, blank=True, null=True)
    first_name = models.CharField(_('Ism'), max_length=50, blank=False, null=False)
    last_name = models.CharField(_('Familya'), max_length=50, blank=False, null=False)
    image = models.ImageField(default='default_images/user.png', upload_to='Users/%Y/%m/', blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user_id = generate_unique_user_id()
        super().save(*args, **kwargs)

    REQUIRED_FIELDS = ['user_id', 'first_name', 'last_name', 'email']
    USERNAME_FIELD = 'username'
    objects = CustomUserManager()

    def get_full_name(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'

    def __str__(self):
        return self.get_full_name()



