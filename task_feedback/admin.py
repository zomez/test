from django.contrib import admin
from .models import DepPay, RayPay, StatusTask, DepPaySoz, ThemeTask, DepAppointment, DepPayPers, RayPayPers, \
    ThemeTaskPers

# Register your models here.
# admin.site.register()
admin.site.register(ThemeTask)
admin.site.register(DepPay)
admin.site.register(DepAppointment)
admin.site.register(DepPayPers)
admin.site.register(ThemeTaskPers)
admin.site.register(RayPay)
admin.site.register(StatusTask)
admin.site.register(DepPaySoz)
admin.site.register(RayPayPers)