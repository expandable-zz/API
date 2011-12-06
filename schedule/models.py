# -*- coding: utf-8 -*-
from django.db import models
from publications.models import Publication

EVENT_STATUS = (
    ('requested', 'Requested'),
    ('confirmed', 'Confirmed'),
    ('canceled', 'Canceled')
)

LOCATION_TYPE = (
    ('other','Other'),
    ('efrei','Efrei'),
    ('class','Classroom'),
    ('lect','Lecture'),
    ('club','Club')
)

class EventLocation(models.Model):
    label = models.CharField(max_length=64)
    type = models.CharField(max_length=6, choices=LOCATION_TYPE)
    default_status = models.CharField(max_length=10, choices=EVENT_STATUS)

    def __unicode__(self):
        return self.label


class EventCategory(models.Model):
    label = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=6, unique=True)
    default_status = models.CharField(max_length=10, choices=EVENT_STATUS)

    def __unicode__(self):
        return self.label

class Event(Publication):
    description = models.TextField(blank=True)
    category = models.ForeignKey(EventCategory, related_name='events')
    url = models.URLField(blank=True)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    location = models.TextField(blank=True)
    clubs = models.ManyToManyField('clubs.Club', related_name='events', blank=True)
    price = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=EVENT_STATUS)

    def __unicode__(self):
        return self.title