from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^feeds/new', views.newFeed, name = 'NewFeed'),
    url(r'^feeds/', views.feeds, name = 'Feeds'),
    url(r'^$', views.articles, name = 'Articles')
]