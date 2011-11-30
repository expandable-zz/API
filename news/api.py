# -*- coding: utf-8 -*-
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from news.models import News
from clubs.api import ClubResource
from users.api import UserResource

class NewsResource(ModelResource):
    club = fields.ForeignKey(ClubResource,'club')
    author = fields.ForeignKey(UserResource,'author')

    class Meta:
        queryset = News.objects.all()
        resource_name = 'news'
        authorization = Authorization()