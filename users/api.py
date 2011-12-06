# -*- coding: utf-8 -*-
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from users.models import ClassGroup, SecondLanguageGroup, ThirdLanguageGroup, User
from clubs.api import ClubResource
from django.conf.urls.defaults import *
from tastypie.utils import trailing_slash

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

    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['password','salt']
        authorization=Authorization()

    def dehydrate(self, bundle):
        """
        print bundle

        bundle.data['coucou'] = {"coucou1": "pouet", "paf" : "damn"}
        """
        return bundle
