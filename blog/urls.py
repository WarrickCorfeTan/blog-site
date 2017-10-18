from django.conf.urls import url
from . import views

urlpatterns = [
	#takes an empty string.
	url(r'^$', views.post_list, name='post_list'),
	#anything starting with post/ then takes anything in the bracket and stores in var pk which is passed to the view (which has to be at least 1 digit) + '/' at the end
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]