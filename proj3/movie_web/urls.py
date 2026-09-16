from django.urls import path
from . import views

urlpatterns = [
    # Public
    path('', views.home, name='home'),
    path('movie/<int:pk>/', views.movie_details, name='movie_detail'),
    path('search/', views.search_movies, name='search_movies'),

    # Watchlist (called by JS fetch)
    path('watchlist/', views.watchlist_view, name='watchlist'),
    path('watchlist/add/', views.watchlist_add, name='watchlist_add'),
    path('watchlist/remove/', views.watchlist_remove, name='watchlist_remove'),

    # Upload
    path('upload/', views.upload_movie, name='upload_movie'),

    # Auth
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]