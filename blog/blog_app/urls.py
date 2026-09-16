from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
    path('edit/<slug:slug>/', views.post_edit, name='post_edit'),
    path('delete/<slug:slug>/', views.post_delete, name='post_delete'),

    path('friends/', views.friends_feed, name='friends_feed'),

    path('follow/<str:username>/', views.follow_user, name='follow_user'),
    path('unfollow/<str:username>/', views.unfollow_user, name='unfollow_user'),
]