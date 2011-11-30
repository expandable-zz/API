# -*- coding: utf-8 -*-
from django.db import models
from users.models import User

VISIBILITY = (
    (0, 'Public'),
    (1, 'Hidden'),
    (2, 'Restricted'),
    (3, 'Rank Restricted'),
    (4, 'Club Restricted')
    )

class Tag(models.Model):
    name = models.CharField(max_length=16, unique=True)
    slug = models.SlugField(max_length=16, unique=True)

    def __unicode__(self):
        return self.name

class Publication(models.Model):
    post_date = models.DateTimeField()
    edit_date = models.DateTimeField(null=True)
    author =  models.ForeignKey(User, related_name='publications')
    visibility = models.IntegerField(choices=VISIBILITY)

    def __unicode__(self):
        return self.pk


class Comment(models.Model):
    post_date = models.DateTimeField()
    content = models.TextField(blank=True)
    author =  models.ForeignKey(User, related_name='comments')
    publication = models.ForeignKey(Publication, related_name='comments')

    def __unicode__(self):
        return self.pk