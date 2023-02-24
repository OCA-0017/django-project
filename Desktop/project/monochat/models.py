from django.db import models

# Create your models here.

# ユーザー
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# 掲示板
class MonoBoards(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, to_field="id", related_name="user_boards")
    category = models.CharField(max_length=255)
    statement = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
# チャット
class chats(models.Model):
    id = models.AutoField(primary_key=True)
    poster_ID = models.ForeignKey(Users, on_delete=models.CASCADE, to_field="id", related_name="chats_poster")
    reciver_ID = models.ForeignKey(Users, on_delete=models.CASCADE, to_field="id", related_name="chats_reciver")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)