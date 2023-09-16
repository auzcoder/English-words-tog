
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('Foydalanuvchi uchun username kerak.')
        if not email:
            raise ValueError('Foydalanuvchi uchun e-mail manzili kerak.')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff qiymati True bo\'lishi kerak.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser qiymati True bo\'lishi kerak.')

        return self.create_user(username, email, password, **extra_fields)
