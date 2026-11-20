from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('post/',views.post, name='post'),
    path('api/books/',views.pages_list),
    path('api/books/<int:pk>/',views.pages_detail),
    path('api/post/create/',views.page_post),
    path('api/books/search/',views.page_search),
]