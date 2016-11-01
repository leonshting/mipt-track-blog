from django.conf.urls import url
from django.views.decorators.http import require_POST

from .models import Post
from .views import *
from django.conf import settings

urlpatterns = [
    url(r'^posts/$', PostList.as_view(), name="post_list"),
    url(r'^posts/(?P<pk>[0-9]*)/$', PostView.as_view(), name="blog_post"),
    url(r'^$', LatestList.as_view(), name="latest_list"),
    url(r'^posts/(?P<pk>[0-9]*)/edit/$', EditPost.as_view(), name="edit_post"),
    url(r'^posts/new/$', login_required(NewPost.as_view()), name="new_post"),
    url(r'^posts/setlike/$', login_required(require_POST(CatchLikeView)), name='setlike')
]
