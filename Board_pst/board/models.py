from django.contrib.auth.models import User
from django.db import models


class Authors(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Имя автора: {self.user.username}'


class Categories(models.Model):
    name_category = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'Название категории: {self.name_category}'


class Posts(models.Model):
    post_title = models.CharField(max_length=100, default='Unnamed')
    post_text = models.TextField(default='Text')
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Заголовок: {self.post_title} Текст статьи: {self.post_text[:30]}...'


class Post_Category(models.Model):
    ...


class News(models.Model):
    ...


class Responds(models.Model):
    ...





