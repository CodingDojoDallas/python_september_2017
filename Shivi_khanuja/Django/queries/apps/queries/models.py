# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    age = models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {} {} {}".format(self.first_name, self.last_name, self.email, self.age)

class Post(models.Model):
    content = models.TextField()
    user=models.ForeignKey(User,related_name="posts")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return "{}".format(self.content)


class Book(models.Model):
    title=models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name="book")
    user=models.ForeignKey(User, related_name="created_books")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return "{}".format(self.title, self.author)