# -*- coding: utf-8 -*-
from tastypie import fields
from tastypie.resources import ModelResource
from system.models import Permission, Rank, Application, Session
from system.authentication import ApiAuthentication

class PermissionResource(ModelResource):
    class Meta:
        queryset = Permission.objects.all()
        resource_name = 'permission'

class RankResource(ModelResource):
    parent = fields.ForeignKey('self', 'parent', null=True)
    permissions = fields.ToManyField(PermissionResource, 'permissions', related_name='ranks', null=True)

    class Meta:
        queryset = Rank.objects.all()
        resource_name = 'rank'

class ApplicationResource(ModelResource):
    permissions = fields.ToManyField(PermissionResource, 'permissions', related_name='applications', null=True)
    club = fields.ForeignKey('clubs.api.ClubResource', 'club')

    class Meta:
        queryset = Application.objects.all()
        resource_name = 'application'

class SessionResource(ModelResource):
    parent = fields.ForeignKey('self', 'parent', null=True)
    application = fields.ForeignKey(ApplicationResource, 'application')
    user = fields.ForeignKey('users.api.UserResource', 'user')

    class Meta:
        queryset = Session.objects.all()
        resource_name = 'session'