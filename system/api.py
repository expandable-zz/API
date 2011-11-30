# -*- coding: utf-8 -*-
from tastypie import fields
from tastypie.resources import ModelResource
from system.models import Permission, Rank, Application, Session
from system.authentication import ApiAuthentication

class PermissionResource(ModelResource):
    class Meta:
        queryset = Permission.objects.all()
        resource_name = 'permission'
        authentication = ApiAuthentication()

class RankResource(ModelResource):
    parent = fields.ForeignKey('self', 'parent')
    class Meta:
        queryset = Rank.objects.all()
        resource_name = 'rank'

class ApplicationResource(ModelResource):
    class Meta:
        queryset = Application.objects.all()
        resource_name = 'application'

class SessionResource(ModelResource):
    class Meta:
        queryset = Session.objects.all()
        resource_name = 'session'