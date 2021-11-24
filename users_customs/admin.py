from django.contrib import admin

# Register your models here.
from users_customs.models import CustomUser, CustomDepartments

admin.site.register(CustomUser)
admin.site.register(CustomDepartments)