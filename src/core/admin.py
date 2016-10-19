# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional', {'fields': ('avatar',)}),
    )

    def admin_avatar(self, instance):
        return instance.avatar and u'<img src="{0}" width="100px" />'.format(
            instance.avatar.url
        )

    admin_avatar.allow_tags = True
    admin_avatar.short_description = u'Аватар'


# Register your models here.
admin.site.register(User, UserAdmin)
