# -*- coding: utf-8 -*-
from django.db import models
from system.models import VISIBILITY
from users.models import User


class Tag(models.Model):
    name = models.CharField(max_length=16, unique=True)
    slug = models.SlugField(max_length=16, unique=True)

    def __unicode__(self):
        return self.name

class Publication(models.Model):
    title = models.CharField(max_length=64, unique=True)
    post_date = models.DateTimeField()
    edit_date = models.DateTimeField(null=True)
    author =  models.ForeignKey(User, related_name='publications')
    visibility = models.IntegerField(choices=VISIBILITY)
    tags = models.ManyToManyField(Tag, related_name='publications')

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    post_date = models.DateTimeField()
    content = models.TextField(blank=True)
    author =  models.ForeignKey(User, related_name='comments')
    publication = models.ForeignKey(Publication, related_name='comments')

    def __unicode__(self):
        return u"%s - %s" % (self.author,self.content[0:32])