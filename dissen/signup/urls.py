from django.conf.urls import url

from . import views

urlpatterns = [
    # /signup/
    url(r'^$', views.index, name='index'),

    # /signup/signup_form
    url(r'signup_form$', views.signup_form, name='signup_form'),

    # /signup/signup_complete
    url(r'signup_complete$', views.signup_complete, name='signup_complete')
]
