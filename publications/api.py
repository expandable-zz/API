# -*- coding: utf-8 -*-
from tastypie import fields
from tastypie.resources import ModelResource
from publications.models import Comment, Tag

class TagResource(ModelResource):
    class Meta:
        queryset = Tag.objects.all()
        resource_name = 'tag'

class CommentResource(ModelResource):
    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comment'