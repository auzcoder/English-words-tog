
from django.contrib.auth.models import BaseUserManager

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('Email address must be provided.')
#         if not user_id:
#             raise ValueError(_('The user_id field must be set'))
#         if not username:
#             raise ValueError(_('The username field must be set'))
#         if not first_name:
#             raise ValueError(_('The First Name field must be set'))
#         if not last_name:
#             raise ValueError(_('The lastname field must be set'))
#
#         # email = self.normalize_email(email)
#         username = self.normalize_username(username)
#         user = self.model(email=email, username=username, user_id=user_id, first_name=first_name, last_name=last_name, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#     def create_superuser(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError(_('Superuser must have is_staff=True.'))
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError(_('Superuser must have is_superuser=True.'))
#
#         return self.create_user(username, user_id, first_name, last_name, email, password, **extra_fields)


# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('Foydalanuvchi uchun e-mail manzili bo\'lishi kerak.')
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, username, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('is_staff qiymati True bo\'lishi kerak.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('is_superuser qiymati True bo\'lishi kerak.')
#
#         return self.create_user(username, email, password, **extra_fields)



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
    