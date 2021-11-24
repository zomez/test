from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, last_name, first_name, **extra_fields):
        """Функция создания обычного пользователя"""
        if not email:
            raise ValueError(_('The email must be set. Please enter email!'))
        if not password:
            raise ValueError(_('The password must be set. Please enter password!'))
        if not last_name:
            raise ValueError(_('The last name must be set. Please enter last name!'))
        if not first_name:
            raise ValueError(_('The first name must be set. Please enter first name!'))
        email = self.normalize_email(email)
        user = self.model(email=email, last_name=last_name, first_name=first_name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """Функция создания супер пользователя"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)