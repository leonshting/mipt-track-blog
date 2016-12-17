from __future__ import unicode_literals

from django.db import models


from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


# Create your models here.


class Like(models.Model):

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    author = models.ForeignKey('core.User', db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s" % self.id


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey('core.User', db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = GenericRelation(Like)

    def __unicode__(self):
        return u"%s" % self.id


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey('Post', db_index=True)
    author = models.ForeignKey('core.User', db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = GenericRelation(Like)

    def __unicode__(self):
        return u"%s" % self.id

    def __str__(self):
        return u"%s" % self.text
