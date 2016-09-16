from django.conf.urls import url

from . import views

urlpatterns = [
    # /signup/
    url(r'^$', views.index, name='index'),

    # /signup/signup_form
    url(r'signup_form$', views.SignupForm.as_view(), name='signup_form')
]
