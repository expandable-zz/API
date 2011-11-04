# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class EventCategory(models.Model):
    label = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=6, unique=True)

    def __unicode__(self):
        return self.label

class Event(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    category = models.ForeignKey(EventCategory, related_name='events')
    url = models.URLField(blank=True)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    location = models.TextField(blank=True)
    clubs = models.ManyToManyField('clubs.Club', related_name='events', blank=True)
    private = models.BooleanField()
    validated = models.NullBooleanField(default=None)
    canceled = models.BooleanField(default=False)
    price = models.IntegerField(default=0)
    minors_allowed = models.BooleanField()

    def __unicode__(self):
        return self.title