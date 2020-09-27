from django.conf.urls import url
from user import views as users_views
urlpatterns = [
    url(r'^getlistpic', users_views.getlistpic, name='home'),
    url(r'^getlist', users_views.getlist, name='home')
]