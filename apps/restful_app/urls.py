from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.users),
    url(r'^users$', views.users),
    url(r'^users/(?P<user_id>\d+)$', views.show),
    url(r'^users/new$', views.new),
    url(r'^users/(?P<user_id>\d+)/edit$', views.edit),
    url(r'^users/(?P<user_id>\d+)/delete$', views.destroy_user),
    url(r'^users/create$', views.create_process),
    url(r'^edit_process$', views.edit_process)
]