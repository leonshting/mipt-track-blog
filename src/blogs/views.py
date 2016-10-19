from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post, Comment
from django.db.models import Count


# Create your views here.

class PostList(ListView):
    template_name = "post_list.html"
    model = Post
    context_object_name = 'post'

    def get_queryset(self):
        qs = super(PostList, self).get_queryset()

        autor = self.request.GET.get("author")
        if autor:
            qs = qs.filter(author__username__contains=autor)

        return qs

    def get_context_data(self, **kwargs):
        data = super(PostList, self).get_context_data(**kwargs)
        data["likes"] = [(i, len(i.likes.all())) for i in self.object_list]
        return data


class PostView(DetailView):
    template_name = "post_detailed.html"
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        data = super(PostView, self).get_context_data(**kwargs)
        data["likes"] = len(self.get_object().likes.all())
        data["comments"] = [i.__str__() for i in self.get_object().comment_set.all()]
        return data


class LatestList(ListView):
    template_name = "post_list.html"
    # model = Post
    queryset = Post.objects.annotate(lc=Count('likes')).order_by('-created_at')[:2]
    context_object_name = 'post'

    # def get_context_data(self, **kwargs):
    #     data = super(LatestList, self).get_context_data(**kwargs)
    #     data["likes"] = [(i, len(i.likes.all())) for i in self.object_list.order_by('-created_at')[:2]]
    #     return data
