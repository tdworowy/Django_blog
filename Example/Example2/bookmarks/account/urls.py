from django.conf.urls import url, include
from django.contrib.auth import admin

from Example.Example2.bookmarks.account import views

urlpatterns = [
    url(r'^login/$',views.user_login,name='login')

]