# -*- coding: utf-8 -*-
from django.db import models

VISIBILITY = (
    (0, 'Public'),
    (1, 'Hidden'),
    (2, 'Restricted'),
    (3, 'Rank Restricted'),
    (4, 'Club Restricted')
    )

class Permission(models.Model):
    name = models.CharField(max_length=48, unique=True)
    label = models.CharField(max_length=64, blank=True)

    def __unicode__(self):
        return self.name

class Rank(models.Model):
    name = models.CharField(max_length=20, unique=True)
    parent = models.ForeignKey('self', null=True)
    permissions = models.ManyToManyField(Permission, related_name='ranks', null=True)

    def __unicode__(self):
        return self.name

class Application(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True)
    api_key = models.CharField(max_length=40, unique=True)
    url = models.URLField(blank=True)
    permissions = models.ManyToManyField(Permission, related_name='applications', null=True)
    club = models.ForeignKey('clubs.Club', related_name='applications')

    def __unicode__(self):
        return self.name

    def has_authorization(self, name, club = None):
        for permission in self.permissions.iterator():
            if permission.name == ('global.%s' % name):
                return True

            if permission.name == name and club == self.club:
                return True
        return False

class Session(models.Model):
    token = models.CharField(max_length=40, unique=True)
    parent = models.ForeignKey('self', null=True)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    user = models.ForeignKey('users.User', related_name='sessions')
    application = models.ForeignKey(Application, related_name='sessions')

    def __unicode__(self):
        return self.token