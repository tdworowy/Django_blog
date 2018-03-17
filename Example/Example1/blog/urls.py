"""example1 URL Configuration

"""
from django.conf.urls import url
from django.contrib import admin
from .feeds import LatestPostsFeed

from Example.Example1.blog import views
app_name = 'blog'
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    # url(r'^$',views.PostListView.as_view(),name='post_list'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'
        r'(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),
    url(r'^feed/$', LatestPostsFeed(), name='post_feed'),
]
