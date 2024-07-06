from django.urls import path
from .views import *
urlpatterns = [
    path('', display_tweet, name='display_tweet'),
    path('create/', create_tweet, name='create_tweet'),
    path('<int:id>/update/', update_tweet, name='update_tweet'),
    path('<int:id>/delete/', delete_tweet, name='delete_tweet'),
    path('register/', register, name='register'),
   
]
