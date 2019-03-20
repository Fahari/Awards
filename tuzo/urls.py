from django.conf.urls import url
from .views import PostListView,PostDetailView
from . import views

urlpatterns=[
    url('^$',PostListView.as_view(),name = 'home'),
    url(r'^post/<int:pk>/',PostDetailView.as_view(),name = 'post-detail'),
    url(r'^profile/', views.profile, name='profile'),


]
