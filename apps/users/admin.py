from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    pass
