from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class Chapter(models.Model):
    """Разделы ОСВ, ОВП, ПЕРСУЧЕТ, НАЗНАЧЕНИЕ"""

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    name_chapter = models.CharField(verbose_name=_('Название раздела'), max_length=40)
    id_name_chapter = models.IntegerField(verbose_name=_('ID Названия раздела'))

    def __str__(self):
        return f'{self.id_name_chapter}. {self.name_chapter}'


class TaskArea(models.Model):
    """Район задачи"""

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Район'

    name_area = models.CharField(verbose_name=_('Название района'), max_length=70)
    reduction_name_area = models.CharField(verbose_name=_('Сокращение'), max_length=25)
    id_name_area = models.IntegerField(verbose_name=_('ID Района'))

    def __str__(self):
        return f'{self.id_name_area}. {self.name_area}'


class ThemeTask(models.Model):
    """Список тем заявок"""

    class Meta:
        verbose_name = 'Тема заявки'
        verbose_name_plural = 'Темы заявок'

    id_theme_task = models.IntegerField(verbose_name=_('Id номер темы'))
    name_theme_task = models.CharField(verbose_name=_('Название темы'), max_length=400)
    comment = models.TextField(verbose_name=_('Коментарий'), blank=True)
    reduction_name_theme_task = models.CharField(verbose_name=_('Сокращение'), max_length=25)

    # color = models.CharField(verbose_name=_('Цвет'), max_length=10)

    def __str__(self):
        return f'{self.name_theme_task}. {self.name_theme_task}'


class StatusTask(models.Model):
    class Meta:
        verbose_name = 'Статус заявки'
        verbose_name_plural = 'Статус заявок'

    name_status = models.CharField(verbose_name=_('Имя статуса'))
    color_status = models.CharField(verbose_name=_('Цвет статуса'))

    def __str__(self):
        return f'{self.name_status}'


class FeedBackTask(models.Model):
    class Meta:
        verbose_name = _('Звонок')
        verbose_name_plural = _('Звонки')

    date_create_task = models.DateTimeField(verbose_name=_('Дата создания заявки'), auto_now=True)
    date_take_task = models.DateTimeField(verbose_name=_('Дата взятие заявки'))
    date_end_task = models.DateTimeField(verbose_name=_('Дата окончания заявки'))

    snils = models.CharField(verbose_name=_('Снилс'), max_length=20)
    fio = models.CharField(verbose_name=_('ФИО'), max_length=100)
    telephone_task = models.CharField(verbose_name=_('Контактный телефон'), max_length=50)
    telephone_contact = models.CharField(verbose_name=_('Телефон для обратной связи'), max_length=50)

    chapter_task = models.ForeignKey(Chapter, on_delete=models.CASCADE, verbose_name=_('Раздел'))
    theme_task = models.ForeignKey(ThemeTask, on_delete=models.CASCADE, verbose_name=_('Тема'))
    area_task = models.ForeignKey(TaskArea, on_delete=models.CASCADE, verbose_name=_('Район'))

    status = models.ForeignKey(StatusTask, on_delete=models.CASCADE, verbose_name=_('Статус'))
    comment = models.TextField(verbose_name=_('Коментарий'))

    user_task_created = models.ForeignKey(User, on_delete=models.SET('Удалено'), verbose_name=_('Создатель'))
    user_task_completed = models.ForeignKey(User, on_delete=models.SET('Удалено'), verbose_name=_('Кто закрыл звонок'))