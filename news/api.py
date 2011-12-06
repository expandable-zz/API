# -*- coding: utf-8 -*-
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from news.models import News
from clubs.api import ClubResource
from users.api import UserResource
from publications.api import PublicationResource

class NewsResource(PublicationResource):
    club = fields.ForeignKey(ClubResource,'club')

    class Meta:
        queryset = News.objects.all()
        resource_name = 'news'
        authorization = Authorization()