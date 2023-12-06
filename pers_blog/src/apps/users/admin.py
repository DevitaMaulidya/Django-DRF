from django.contrib import admin
from apps.users.models import UsersModel

# Register your models here.
class UsersModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(UsersModel, UsersModelAdmin)