from django.forms import ModelForm
from django.http import HttpResponseForbidden, HttpResponseRedirect, Http404
from django.shortcuts import resolve_url, get_list_or_404
from django.views.decorators.http import require_POST
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, FormMixin, ModelFormMixin
from .models import Post, Comment, Like
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from .forms import *


# Create your views here.
@login_required
@require_POST
def CatchLikeView(request):
    try:
        post = Post.objects.get(id=int(request.POST['id']))
        print("here")
        if not post.likes.all().filter(author=request.user).exists():
            like = Like(content_object=post, author=request.user)
            like.save()
    except Post.DoesNotExist:
        raise Http404("You are trying to like non-existing post")
    return HttpResponseRedirect(request.POST['redirect_url'])


class PostList(ListView):
    template_name = "post_list.html"
    model = Post
    context_object_name = 'posts'
    paginate_by = 10
    queryset = Post.objects.annotate(lc=Count('likes'))

    def get_queryset(self):
        qs = super(PostList, self).get_queryset()
        author = self.request.GET.get("author")
        sort = self.request.GET.get("sort")
        if author:
            qs = get_list_or_404(qs.filter(author__username__contains=author))
        if sort:
            if (sort == 'earlier'):
                qs = get_list_or_404(qs.order_by('-created_at'))
            elif sort == 'later':
                qs = get_list_or_404(qs.order_by('created_at'))
            elif sort == 'liked':
                qs = qs.order_by('-lc')
        return qs



class PostView(FormMixin, DetailView):
    template_name = "post_detailed.html"
    model = Post
    form_class = CommentForm
    queryset = Post.objects.annotate(lc=Count('likes'))

    def get_context_data(self, **kwargs):
        data = super(PostView, self).get_context_data(**kwargs)
        data["post"] = self.get_object();
        data["comments"] = [i for i in self.get_object().comment_set.all()]
        data["commentlikes"] = [len(i.likes.all()) for i in data["comments"]]
        data["form"] = self.get_form(form_class=self.form_class)
        if not self.request.user.is_anonymous and self.get_object().likes.all().filter(
                author=self.request.user).exists():
            data["liked"] = True
        else:
            data["liked"] = False
        return data

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form(form_class=self.form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(PostView, self).form_valid(form)

    def get_form(self, form_class=None):
        form = super(PostView, self).get_form(form_class)
        if (not self.request.user.is_anonymous):
            form.instance.author = self.request.user
            form.instance.post = self.get_object()
        else:
            form = None
        return form

    def get_success_url(self):
        return resolve_url('blogs:blog_post', self.kwargs['pk'])
        # olololo


class LatestList(ListView):
    paginate_by = 10
    template_name = "post_list.html"
    queryset = Post.objects.annotate(lc=Count('likes')).order_by('-created_at')[:10]
    context_object_name = 'posts'




class EditPost(UpdateView):
    def get_success_url(self):
        return resolve_url('blogs:blog_post', pk=self.object.pk)

    def dispatch(self, request, *args, **kwargs):
        handler = super(EditPost, self).dispatch(request, *args, **kwargs)
        if self.object.author != request.user:
            return HttpResponseForbidden(u"U cant touch this.")
        return handler

    def get_context_data(self, **kwargs):
        cd = super(EditPost, self).get_context_data(**kwargs)
        cd['create'] = False
        return cd
    template_name = "edit.html"
    model = Post
    form_class = PostForm


class NewPost(CreateView):
    template_name = "edit.html"
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return resolve_url('blogs:blog_post', self.object.pk)

    def get_form(self, form_class=None):
        form = super(NewPost, self).get_form(form_class)
        form.instance.author = self.request.user
        return form

    def get_context_data(self, **kwargs):
        cd = super(NewPost, self).get_context_data(**kwargs)
        cd['create'] = True
        return cd
