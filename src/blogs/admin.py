from django.contrib import admin
from .models import Post, Comment, Like


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


class LikeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Like)
