from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    #path( '', views.monochat, name='monochat' ),
    path( '', views.login, name='login' ),
    path( 'register', views.register, name='register' ),

    # boards
    path('boards/', views.boards, name="boards"),
    path('boards/<str:category>', views.getBoardsCategory, name="getBoardsCategory"),
    

    # chat
    path('monochat/', views.index, name='index'),
    path('monochat/<str:room_name>/', views.room, name='room'),

    path('homepage/', views.homepage, name="homepage"),
]