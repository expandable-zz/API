# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from tastypie.api import Api
from users.api import ClassGroupResource, SecondLanguageGroupResource, ThirdLanguageGroupResource, UserResource
from clubs.api import ClubCategoryResource, ClubResource
from schedule.api import EventCategoryResource, EventResource
from news.api import NewsResource
from publications.api import CommentResource, TagResource
from system.api import RankResource, PermissionResource, ApplicationResource, SessionResource

v1_api = Api(api_name='v1')
#users
v1_api.register(ClassGroupResource())
v1_api.register(SecondLanguageGroupResource())
v1_api.register(ThirdLanguageGroupResource())
v1_api.register(UserResource())
#clubs
v1_api.register(ClubCategoryResource())
v1_api.register(ClubResource())
#schedule
v1_api.register(EventCategoryResource())
v1_api.register(EventResource())
#news
v1_api.register(NewsResource())
#publications
v1_api.register(TagResource())
v1_api.register(CommentResource())
#system
v1_api.register(RankResource())
v1_api.register(PermissionResource())
v1_api.register(ApplicationResource())
v1_api.register(SessionResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'api.views.home', name='home'),
    # url(r'^api/', include('api.foo.urls')),
    url(r'^', include(v1_api.urls)),
    url(r'^$', 'users.views.home', name='home'),
    url(r'^init$', 'users.views.init', name='init')
)
