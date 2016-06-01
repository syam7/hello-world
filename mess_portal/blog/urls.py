from django.conf.urls import url

from blog import views
app_name ='blog'
urlpatterns =[
	url (r'^$',views.index,name='index'),
	url (r'^add_question',views.add_question,name='question'),
	url(r'^question/(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
	url(r'^question/(?P<question_id>[0-9]+)/handling/$',views.handling,name='handling'),
]
