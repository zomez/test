from django.db import models
from django.utils.translation import ugettext_lazy as _

from users_customs.models import CustomDepartments, CustomUser


class ThemeTask(models.Model):
    """Список тем заявок"""

    class Meta:
        verbose_name = 'Тема заявки Соц.Выплат'
        verbose_name_plural = 'Темы заявок Соц.Выплаты'

    id_theme_task = models.IntegerField(verbose_name=_('Id номер темы'))
    name_theme_task = models.CharField(verbose_name=_('Название темы'), max_length=400)
    comment = models.TextField(verbose_name=_('Коментарий'), blank=True)
    reduction_name_theme_task = models.CharField(verbose_name=_('Сокращение'), max_length=25)

    # color = models.CharField(verbose_name=_('Цвет'), max_length=10)

    def __str__(self):
        return f'{self.name_theme_task}. {self.name_theme_task}'


class ThemeTaskPers(models.Model):
    """Список тем заявок"""

    class Meta:
        verbose_name = 'Тема заявки Перс.учет'
        verbose_name_plural = 'Темы заявок Перс.учета'

    id_theme_task = models.IntegerField(verbose_name=_('Id номер темы'))
    name_theme_task = models.CharField(verbose_name=_('Название темы'), max_length=400)
    comment = models.TextField(verbose_name=_('Коментарий'), blank=True)
    reduction_name_theme_task = models.CharField(verbose_name=_('Сокращение'), max_length=25)

    # color = models.CharField(verbose_name=_('Цвет'), max_length=10)

    def __str__(self):
        return f'{self.name_theme_task}. {self.name_theme_task}'


class RayPay(models.Model):
    class Meta:
        verbose_name = _('Район Выплаты')
        verbose_name_plural = _('Районы Выплаты')

    department = models.ForeignKey(CustomDepartments, on_delete=models.CASCADE, verbose_name=_('Отдел'))
    name_ray = models.CharField(verbose_name=_('Название района'), max_length=60)
    reduction_name_ray = models.CharField(verbose_name=_('Сокращение название района'), max_length=20)
    number_code_ray = models.CharField(verbose_name=_('Числовой код района'), max_length=20)

    def __str__(self):
        return f'{self.number_code_ray}. {self.name_ray}'


class RayAppointment(models.Model):
    class Meta:
        verbose_name = _('Район Назначения')
        verbose_name_plural = _('Районы Назначения')

    department = models.ForeignKey(CustomDepartments, on_delete=models.CASCADE, verbose_name=_('Отдел'))
    name_ray = models.CharField(verbose_name=_('Название района'), max_length=60)
    reduction_name_ray = models.CharField(verbose_name=_('Сокращение название района'), max_length=20)
    number_code_ray = models.CharField(verbose_name=_('Числовой код района'), max_length=20)

    def __str__(self):
        return f'{self.number_code_ray}. {self.name_ray}'


class RayPaySoz(models.Model):
    class Meta:
        verbose_name = _('Район Назначения')
        verbose_name_plural = _('Районы Назначения')

    department = models.ForeignKey(CustomDepartments, on_delete=models.CASCADE, verbose_name=_('Отдел'))
    name_ray = models.CharField(verbose_name=_('Название района'), max_length=60)
    reduction_name_ray = models.CharField(verbose_name=_('Сокращение название района'), max_length=20)
    number_code_ray = models.CharField(verbose_name=_('Числовой код района'), max_length=20)

    def __str__(self):
        return f'{self.number_code_ray}. {self.name_ray}'


class RayPayPers(models.Model):
    class Meta:
        verbose_name = _('Район Перс.Учет')
        verbose_name_plural = _('Районы Перс.Учета')

    department = models.ForeignKey(CustomDepartments, on_delete=models.CASCADE, verbose_name=_('Отдел'))
    name_ray = models.CharField(verbose_name=_('Название района'), max_length=60)
    reduction_name_ray = models.CharField(verbose_name=_('Сокращение название района'), max_length=20)
    number_code_ray = models.CharField(verbose_name=_('Числовой код района'), max_length=20)

    def __str__(self):
        return f'{self.number_code_ray}. {self.name_ray}'


class StatusTask(models.Model):
    class Meta:
        verbose_name = 'Статус заявки'
        verbose_name_plural = 'Статус заявок'

    name_status = models.CharField(verbose_name=_('Имя статуса'), max_length=50)
    color_status = models.CharField(verbose_name=_('Цвет статуса'), max_length=20)

    def __str__(self):
        return f'{self.name_status}'


###############################################################################################################


class DepPay(models.Model):
    class Meta:
        verbose_name = _('Задача Выплата')
        verbose_name_plural = _('Задачи Выплаты')

    user_create_task = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_('Создатель заявки'),
                                         related_name='user_create_task_pay')

    date_create_task = models.DateTimeField(verbose_name=_('Дата создания заявки'), auto_now=True)
    date_take_task = models.DateTimeField(verbose_name=_('Дата взятие заявки'), blank=True, null=True)
    date_end_task = models.DateTimeField(verbose_name=_('Дата окончания заявки'), blank=True, null=True)

    snils = models.CharField(verbose_name=_('Снилс'), max_length=20)
    fio = models.CharField(verbose_name=_('ФИО'), max_length=100)
    telephone_task = models.CharField(verbose_name=_('Контактный телефон'), max_length=50)
    telephone_contact = models.CharField(verbose_name=_('Телефон для обратной связи'), max_length=50)
    question = models.TextField(verbose_name=_('Вопрос'))
    time_call = models.CharField(max_length=150, verbose_name=_('Дата и время обратного звонка'))
    ray = models.ForeignKey(RayPay, on_delete=models.CASCADE, verbose_name=_('Район'), blank=True, null=True)
    note = models.TextField(verbose_name=_('Примечание'), blank=True)
    status = models.ForeignKey(StatusTask, verbose_name=_('Статус'), on_delete=models.CASCADE, blank=True, null=True)

    user_close_task = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_('Завершивший заявку'),
                                        related_name='user_close_task_pay', blank=True, null=True)

    def __str__(self):
        return f'{self.date_create_task}/{self.snils}'


class DepAppointment(models.Model):
    class Meta:
        verbose_name = _('Задача Назначение')
        verbose_name_plural = _('Задачи Назначения')

    user_create_task = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_('Создатель заявки'),
                                         related_name='user_create_task_appointment')

    date_create_task = models.DateTimeField(verbose_name=_('Дата создания заявки'), auto_now=True)
    date_take_task = models.DateTimeField(verbose_name=_('Дата взятие заявки'), blank=True, null=True)
    date_end_task = models.DateTimeField(verbose_name=_('Дата окончания заявки'), blank=True, null=True)

    snils = models.CharField(verbose_name=_('Снилс'), max_length=20)
    fio = models.CharField(verbose_name=_('ФИО'), max_length=100)
    telephone_task = models.CharField(verbose_name=_('Контактный телефон'), max_length=50)
    telephone_contact = models.CharField(verbose_name=_('Телефон для обратной связи'), max_length=50)
    question = models.TextField(verbose_name=_('Вопрос'))
    time_call = models.CharField(max_length=150, verbose_name=_('Дата и время обратного звонка'))
    ray = models.ForeignKey(RayAppointment, on_delete=models.CASCADE, verbose_name=_('Район'))
    note = models.TextField(verbose_name=_('Примечание'))
    status = models.ForeignKey(StatusTask, verbose_name=_('Статус'), on_delete=models.CASCADE)

    user_close_task = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_('Завершивший заявку'),
                                        related_name='user_close_task_appointment', blank=True, null=True)

    def __str__(self):
        return f'{self.date_create_task}/{self.snils}'


class DepPaySoz(models.Model):
    class Meta:
        verbose_name = _('Задача Соц.выплата')
        verbose_name_plural = _('Задачи Соц.выплаты')

    user_create_task = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_('Создатель заявки'),
                                         related_name='user_create_task_pay_soz')

    date_create_task = models.DateTimeField(verbose_name=_('Дата создания заявки'), auto_now=True)
    date_take_task = models.DateTimeField(verbose_name=_('Дата взятие заявки'), blank=True, null=True)
    date_end_task = models.DateTimeField(verbose_name=_('Дата окончания заявки'), blank=True, null=True)

    snils = models.CharField(verbose_name=_('Снилс'), max_length=20)
    fio = models.CharField(verbose_name=_('ФИО'), max_length=100)
    telephone_task = models.CharField(verbose_name=_('Контактный телефон'), max_length=50)
    telephone_contact = models.CharField(verbose_name=_('Телефон для обратной связи'), max_length=50)
    theme_task = models.ForeignKey(ThemeTask, on_delete=models.CASCADE, verbose_name=_('Тема заявки'))
    question = models.TextField(verbose_name=_('Вопрос'))
    time_call = models.CharField(max_length=150, verbose_name=_('Дата и время обратного звонка'))
    ray = models.ForeignKey(RayAppointment, on_delete=models.CASCADE, verbose_name=_('Район'))
    note = models.TextField(verbose_name=_('Примечание'))
    status = models.ForeignKey(StatusTask, verbose_name=_('Статус'), on_delete=models.CASCADE)

    user_close_task = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_('Завершивший заявку'),
                                        related_name='user_close_task_pay_soz', blank=True, null=True)

    def __str__(self):
        return f'{self.date_create_task}/{self.snils}'


class DepPayPers(models.Model):
    class Meta:
        verbose_name = _('Задача Перс.Учет')
        verbose_name_plural = _('Задачи Перс.Учет')

    user_create_task = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_('Создатель заявки'),
                                         related_name='user_create_task_pay_pers')

    date_create_task = models.DateTimeField(verbose_name=_('Дата создания заявки'), auto_now=True)
    date_take_task = models.DateTimeField(verbose_name=_('Дата взятие заявки'), blank=True, null=True)
    date_end_task = models.DateTimeField(verbose_name=_('Дата окончания заявки'), blank=True, null=True)

    snils = models.CharField(verbose_name=_('Снилс'), max_length=20)
    fio = models.CharField(verbose_name=_('ФИО'), max_length=100)
    telephone_task = models.CharField(verbose_name=_('Контактный телефон'), max_length=50)
    telephone_contact = models.CharField(verbose_name=_('Телефон для обратной связи'), max_length=50)
    theme_task = models.ForeignKey(ThemeTaskPers, verbose_name=_('Темы Перс.Учёта'), on_delete=models.CASCADE)
    reg_number = models.IntegerField(verbose_name=_('Рег.Номер'))
    reg_name = models.CharField(max_length=200, verbose_name=_('Наименование страхователя'), blank=True)
    question = models.TextField(verbose_name=_('Вопрос'))
    time_call = models.CharField(max_length=150, verbose_name=_('Дата и время обратного звонка'))
    ray = models.ForeignKey(RayPayPers, on_delete=models.CASCADE, verbose_name=_('Район'))
    note = models.TextField(verbose_name=_('Примечание'))
    status = models.ForeignKey(StatusTask, verbose_name=_('Статус'), on_delete=models.CASCADE)

    user_close_task = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_('Завершивший заявку'),
                                        related_name='user_close_task_pay_pers', blank=True, null=True)

    def __str__(self):
        return f'{self.date_create_task}/{self.snils}'
