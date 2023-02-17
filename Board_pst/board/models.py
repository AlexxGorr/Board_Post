from django.contrib.auth.models import User
from django.db import models

from . import resource


class Authors(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Имя автора: {self.user.username}'


class Posts(models.Model):
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=100, default='')
    post_text = models.TextField(default='')
    date_create = models.DateTimeField(auto_now_add=True)
    name_category = models.CharField(max_length=5, choices=resource.CATEGORIES_SELECT, default='')

    def __str__(self):
        return f'Публикация: {self.post_title} {self.post_text[:30]}... Автор: {self.author}'

    def preview(self):
        return f'{self.post_text[:125]}'


class Responds(models.Model):
    text_respond = models.TextField(max_length=1000)
    date_respond = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    hater = models.ForeignKey(Authors, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text_respond[:50]}...'





