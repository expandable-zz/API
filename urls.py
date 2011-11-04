# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from tastypie.api import Api
from users.api import ClassGroupResource, SecondLanguageGroupResource, ThirdLanguageGroupResource, UserResource
from clubs.api import ClubCategoryResource, ClubResource
from schedule.api import EventCategoryResource, EventResource

v1_api = Api(api_name='v1')
v1_api.register(ClassGroupResource())
v1_api.register(SecondLanguageGroupResource())
v1_api.register(ThirdLanguageGroupResource())
v1_api.register(UserResource())
v1_api.register(ClubCategoryResource())
v1_api.register(ClubResource())
v1_api.register(EventCategoryResource())
v1_api.register(EventResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'api.views.home', name='home'),
    # url(r'^api/', include('api.foo.urls')),
    url(r'^', include(v1_api.urls)),
)
