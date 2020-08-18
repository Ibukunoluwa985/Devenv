from django.urls import path
from . import views

urlpatterns = [
    # create post, reply
    path('create_post',views.create_post, name='create_post'),

    # detail post infomation
    path('<id>',views.post_datail, name='post_datail'),
]