from django.conf.urls import url
from .models import Post
from .views import *

urlpatterns = [
    url(r'^posts/$', PostList.as_view(), name="post_list"),
    url(r'^posts/(?P<pk>[0-9]*)/$', PostView.as_view(), name="blog_post"),
    url(r'^$', LatestList.as_view(), name="latest_list")
]
