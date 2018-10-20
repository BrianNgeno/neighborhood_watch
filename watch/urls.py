from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home_page,name = 'home_page'),
    ]