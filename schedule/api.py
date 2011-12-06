# -*- coding: utf-8 -*-
from tastypie import fields
from tastypie.resources import ModelResource
from schedule.models import EventCategory, EventLocation, Event

class EventLocationResource(ModelResource):
    class Meta:
        queryset = EventLocation.objects.all()
        resource_name = 'event_location'

class EventCategoryResource(ModelResource):
    class Meta:
        queryset = EventCategory.objects.all()
        resource_name = 'event_category'

class EventResource(ModelResource):
    category = fields.ForeignKey(EventCategoryResource, 'category')
    clubs = fields.ToManyField('clubs.ClubResource','clubs',related_name='events')

    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'