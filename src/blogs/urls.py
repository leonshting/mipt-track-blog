from django.conf.urls import url
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_POST, require_GET

from .models import Post
from .views import *
from django.conf import settings

urlpatterns = [
    url(r'^posts/$', cache_page(60)(PostList.as_view()), name="post_list"),
    url(r'^posts/(?P<pk>[0-9]*)/$', PostView.as_view(), name="blog_post"),
    url(r'^posts/(?P<pk>[0-9]*)/getlike/$', login_required(require_GET(get_likes)), name="post_getlikes"),
    url(r'^posts/(?P<pk>[0-9]*)/getcomms/', login_required(require_GET(get_comms)), name="post_getcomms"),
    url(r'^$', cache_page(60)(LatestList.as_view()), name="latest_list"),
    url(r'^posts/(?P<pk>[0-9]*)/edit/$', EditPost.as_view(), name="edit_post"),
    url(r'^posts/new/$', login_required(NewPost.as_view()), name="new_post"),
    url(r'^posts/setlike/$', login_required(require_POST(catch_like_view)), name='setlike')
]
