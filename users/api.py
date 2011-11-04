# -*- coding: utf-8 -*-
from tastypie import fields
from tastypie.resources import ModelResource
from users.models import ClassGroup, SecondLanguageGroup, ThirdLanguageGroup, User
from clubs.api import ClubResource

class ClassGroupResource(ModelResource):
    class Meta:
        queryset = ClassGroup.objects.all()
        resource_name = 'class_group'

class SecondLanguageGroupResource(ModelResource):
    class Meta:
        queryset = SecondLanguageGroup.objects.all()
        resource_name = 'second_language_group'

class ThirdLanguageGroupResource(ModelResource):
    class Meta:
        queryset = ThirdLanguageGroup.objects.all()
        resource_name = 'third_language_group'

class UserResource(ModelResource):
    class_group = fields.ForeignKey(ClassGroupResource, 'class_group')
    second_group = fields.ForeignKey(SecondLanguageGroupResource, 'second_group', null=True)
    third_group = fields.ForeignKey(ThirdLanguageGroupResource, 'third_group', null=True)
    clubs = fields.ManyToManyField(ClubResource, 'clubs')

    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
