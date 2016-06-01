from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^today', views.today, name='today'),
        url(r'^$', views.index, name='index'),
        url(r'^(?P<day_id>[0-9]+)/$', views.detail, name='detail'),
        ]
