from django.urls import path
from . import views

urlpatterns = [
    # auth home page
    path('',views.index, name='index'),
    
    # registration
    path('profile/<username>/',views.profile, name='profile'),
    path('register/',views.registerUser, name='registerUser'),
    path('login/',views.loginUser, name='loginUser'),
    path('logout/',views.logout, name='logout'),

    # extra field update
    path('username_update/',views.username_update, name='username_update'),
    path('first_name_update/',views.first_name_update, name='first_name_update'),
    path('last_name_update/',views.last_name_update, name='last_name_update'),
    path('email_update/',views.email_update, name='email_update'),
    path('github_update/',views.github_update, name='github_update'),
    path('add_repo',views.add_repo, name='add_repo'),

    # activate account
    path('activate_account/',views.activate_account, name='activate_account'),

    # disactivate account
    path('disactivate_account/',views.disactivate_account, name='disactivate_account'),
]