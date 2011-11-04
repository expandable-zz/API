# -*- coding: utf-8 -*-
from tastypie import fields
from tastypie.resources import ModelResource
from clubs.models import ClubCategory, Club

class ClubCategoryResource(ModelResource):
    class Meta:
        queryset = ClubCategory.objects.all()
        resource_name = 'club_category'

class ClubResource(ModelResource):
    category = fields.ForeignKey(ClubCategoryResource, 'category')

    class Meta:
        queryset = Club.objects.all()
        resource_name = 'club'