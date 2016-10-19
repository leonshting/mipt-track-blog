from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings


# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    first_name = models.CharField(('first name'), max_length=30, blank=False)
    email = models.EmailField(('E-mail address'), blank=False, unique=True)

    def image_url(self):

        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return '{}default-avatar.png'.format(settings.STATIC_URL)
