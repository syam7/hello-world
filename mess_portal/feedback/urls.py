from django.conf.urls import url

from feedback import views

urlpatterns =[
	url(r'^$',views.feedback_index,name='feedback_index'),
	url(r'^handling_data',views.handling_data,name='handling_data'),
]
