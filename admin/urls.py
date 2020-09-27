from django.conf.urls import url
from user import views as users_views
urlpatterns = [
    url(r'^getlistpic', users_views.getlistpic, name='home'),
    url(r'^getlist', users_views.getlist, name='home'),
    url(r'^addUser', users_views.addUser, name='home'),
    url(r'^deleteUser', users_views.deleteUser, name='home'),
    url(r'^updateUser', users_views.updateUser, name='home')
]
