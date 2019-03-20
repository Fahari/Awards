from django.conf.urls import url
from .views import PostListView
from . import views

urlpatterns=[
    url('^$',PostListView.as_view(),name = 'home'),
    url(r'^profile/', views.profile, name='profile'),

]
