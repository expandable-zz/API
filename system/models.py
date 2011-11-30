# -*- coding: utf-8 -*-
from django.db import models

class Permission(models.Model):
    name = models.CharField(max_length=32, unique=True)
    label = models.CharField(max_length=64)
    is_global = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class Rank(models.Model):
    name = models.CharField(max_length=20, unique=True)
    parent = models.ForeignKey('self', blank=True)
    permissions = models.ManyToManyField(Permission, related_name='ranks', blank=True)

    def __unicode__(self):
        return self.name

class Application(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True)
    api_key = models.CharField(max_length=40, unique=True)
    url = models.URLField(blank=True)
    permissions = models.ManyToManyField(Permission, related_name='applications', blank=True)
    club = models.ForeignKey('clubs.Club', related_name='applications')

    def __unicode__(self):
        return self.name

class Session(models.Model):
    token = models.CharField(max_length=40, unique=True)
    parent = models.ForeignKey('self', null=True)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    user = models.ForeignKey('users.User', related_name='sessions')
    app = models.ForeignKey(Application, related_name='sessions')

    def __unicode__(self):
        return self.token