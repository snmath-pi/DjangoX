from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', home),
    path('student', post_student),
    path('update-student/<int:id>/', update_student),
    path('delete-student/<int:id>/', delete_student),
    path('get-book/', get_book),
]
