from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import User
from django.views.generic.base import TemplateView


# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['contents'] = "That's a blog!"
        return context


class UserCreationF(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']
