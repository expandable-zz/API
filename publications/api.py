# -*- coding: utf-8 -*-
from tastypie import fields
from tastypie.resources import ModelResource
from publications.models import Comment, Tag, Publication
from users.api import UserResource

class TagResource(ModelResource):
    class Meta:
        queryset = Tag.objects.all()
        resource_name = 'tag'

class CommentResource(ModelResource):
    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comment'

class PublicationResource(ModelResource):
    author = fields.ForeignKey(UserResource,'author')
    tags = fields.ToManyField(TagResource,'tags',related_name='publications')

    class Meta:
        queryset = Publication.objects.all()
        resource_name = 'publication'