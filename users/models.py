# -*- coding: utf-8 -*-
from django.db import models
from clubs.models import Club
from system.models import Rank, VISIBILITY

USER_TYPE = (
    ('student', 'Student'),
    ('prof', 'Professor'),
    ('staff', 'Staff Member'),
    ('former', 'Former')
    )

class Group(models.Model):
    rank = models.ForeignKey(Rank, related_name='groups')
    club = models.ForeignKey(Club, related_name='groups')

    def __unicode__(self):
        return self.pk

class ClassGroup(models.Model):
    label = models.CharField(max_length=8)

    def __unicode__(self):
        return self.label

class SecondLanguageGroup(models.Model):
    label = models.CharField(max_length=8)

    def __unicode__(self):
        return self.label

class ThirdLanguageGroup(models.Model):
    label = models.CharField(max_length=8)

    def __unicode__(self):
        return self.label

class User(models.Model):
    type = models.CharField(max_length=8, choices=USER_TYPE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.SlugField(max_length=8, unique=True)
    birthdate = models.DateField(blank=True)
    photo = models.ImageField(upload_to='photos', max_length=8, blank=True)
    email = models.EmailField(unique=True)
    salt = models.CharField(max_length=10)
    password = models.CharField(max_length=40)
    phone = models.CharField(max_length=10, blank=True)
    title = models.CharField(max_length=48, blank=True)
    groups = models.ManyToManyField(Group, related_name='users')

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)

class UserInfo(models.Model):
    name = models.CharField(max_length=16)
    value = models.CharField(max_length=64)
    visibility = models.IntegerField(choices=VISIBILITY)
    user = models.ForeignKey(User, related_name='info')

    def __unicode__(self):
        return u"%s : %s" % (self.name, self.value)

class StudentDetails(models.Model):
    leaving_year = models.IntegerField()
    class_group = models.ForeignKey(ClassGroup, related_name='details')
    second_group = models.ForeignKey(SecondLanguageGroup, null=True, related_name='details')
    third_group = models.ForeignKey(ThirdLanguageGroup, null=True, related_name='details')
    address = models.CharField(max_length=32)
    post_code = models.CharField(max_length=5)
    city = models.CharField(max_length=20)
    user = models.OneToOneField(User, parent_link=True, related_name='details')

    def __unicode__(self):
        return u"%s %s - P%u" % (self.user.first_name, self.user.last_name, self.leaving_year)