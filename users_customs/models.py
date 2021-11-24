from django.db import models

from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# Перевод текста
from django.utils.translation import ugettext_lazy as _

# Сигналы
# from django.dispatch import receiver
# from django.db.models.signals import post_save

# My class import
from .managers import CustomUserManager


# Create your models here.
class CustomDepartments(models.Model):
    """Модель отдела пользователя"""

    class Meta:
        ordering = ['name_departments', ]
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    # Имя отдела
    name_departments = models.CharField(_('Name of departments'), max_length=30)
    # Сокращенное имя отдела
    reduction_name_departments = models.CharField(max_length=30,
                                                  verbose_name=_('Reduction name of departments'),
                                                  blank=True,
                                                  help_text=_('Enter reduction of name department'))



    def __str__(self):
        return f'{self.reduction_name_departments}'


class CustomGroup(models.Model):
    """Модель групп пользователей"""

    class Meta:
        verbose_name = 'Custom group'
        verbose_name_plural = 'Custom group\'s'
        ordering = ['name_custom_group', ]

    # Имя кастомной группы
    name_custom_group = models.CharField(max_length=30,
                                         verbose_name=_('Name of custom group'),
                                         help_text=_('Enter name of custom group')
                                         )
    # Сокращение имени группы
    reduction_name_group = models.CharField(max_length=30,
                                            verbose_name=_('Reduction of custom group'),
                                            help_text=_('Enter reduction of custom group'),
                                            blank=True)

    def __str__(self):
        return f'{self.reduction_name_group}'


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Модель пользователя"""

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['date_register', ]

    objects = CustomUserManager()

    email = models.EmailField(verbose_name=_('Email Address'), help_text=_('Enter email address'), unique=True)
    last_name = models.CharField(verbose_name=_('Last name'),
                                 help_text=_('Enter last name'),
                                 max_length=30,
                                 blank=False,
                                 )
    first_name = models.CharField(verbose_name=_('First name'),
                                  help_text=_('Enter first name'),
                                  max_length=30,
                                  blank=False,
                                  )
    # Дата последнего входа пользователя
    date_joined = models.DateTimeField(default=timezone.now, verbose_name=_('Date joined'))
    # Дата регистрации
    date_register = models.DateTimeField(auto_now_add=True, verbose_name=_('Date register'))
    # Дата последнего изменения пользователя
    date_edit_user = models.DateTimeField(auto_now=True, verbose_name=_('Date edit user'))

    # Активность пользователя
    is_active = models.BooleanField(default=True, verbose_name=_('Active user'))
    # Супер пользователь
    is_superuser = models.BooleanField(default=False, verbose_name=_('Superuser'))
    # Доступ к админке DJANGO
    is_staff = models.BooleanField(default=False, verbose_name=_('Access to admin site'))
    department = models.ForeignKey(CustomDepartments,
                                   on_delete=models.SET_NULL,
                                   blank=True,
                                   null=True,
                                   verbose_name=_('Department'),
                                   help_text=_('Choice department'),
                                   )
    custom_group = models.ManyToManyField(CustomGroup,
                                          verbose_name=_('Custom groups'),
                                          )

    local_telephone = models.CharField(max_length=20, verbose_name=_('Telephone number'))
    room = models.CharField(max_length=10, verbose_name=_('Room number'))
    ip = models.GenericIPAddressField(verbose_name=_('Ip-address'), default='0.0.0.0')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', ]

    def __str__(self):
        return f'{self.email}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    full_name.short_description = "Full name of the person"
    first_name.admin_order_field = 'last_name'
