from django.conf.urls import url
from django.contrib.auth.views import login, logout
from django.conf import settings
from django.views.generic import CreateView

from .views import HomePageView, UserCreationF

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name="home_page"),
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^loginajax/$', login, {'template_name': 'login_modal.html'}, name='login_ajax'),
    url(r'^logout/$', logout, {'next_page': settings.LOGIN_REDIRECT_URL}, name='logout'),
    url(r'^register/$', CreateView.as_view(template_name='register.html',
                                           form_class=UserCreationF,
                                           success_url='/'), name='register'),
]
