from django.urls import path
from .views import *


urlpatterns = [
    path('', post_list_view, name='post_list'),
    path('<str:tag_name>/', post_list_by_tag_view, name='post_tag_list'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('create/', crete_post, name='post_create'),
]

