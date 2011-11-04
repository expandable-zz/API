# -*- coding: utf-8 -*-
from tastypie import fields
from tastypie.resources import ModelResource
from schedule.models import EventCategory, Event

class EventCategoryResource(ModelResource):
    class Meta:
        queryset = EventCategory.objects.all()
        resource_name = 'event_category'

class EventResource(ModelResource):
    category = fields.ForeignKey(EventCategoryResource, 'category')

    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'