# -*- coding: utf-8 -*-
from django.db import models
from clubs.models import Club

# Create your models here.
class ClassGroup(models.Model):
    CLASS_TYPE_CHOICES = (
        ('P', "Primary"),
        ('2', "Second language"),
        ('3', "Third language"),
    )
    label = models.CharField(max_length=8)
    color = models.CharField(max_length=6, unique=True)
    class_type = models.CharField(max_length=3, choices=CLASS_TYPE_CHOICES)

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.SlugField(max_length=8, unique=True)
    birthdate = models.DateField(blank=True)
    photo = models.ImageField(upload_to='photos', max_length=8, blank=True)
    email = models.EmailField(unique=True)
    salt = models.CharField(max_length=10)
    password = models.CharField(max_length=40)
    leaving_year = models.IntegerField()
    class_group = models.ForeignKey(ClassGroup, related_name='group_set')
    second_group = models.ForeignKey(ClassGroup, null=True, related_name='second_group_set')
    third_group = models.ForeignKey(ClassGroup, null=True, related_name='third_group_set')
    phone_number = models.CharField(max_length=10, blank=True)
    nickname = models.CharField(max_length=20, blank=True)
    clubs = models.ManyToManyField(Club, related_name='clubs_set')