from django.urls import path
from . import views

urlpatterns = [
    # create post
    path('create_post',views.create_post, name='create_post'),
]