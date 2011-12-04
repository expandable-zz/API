# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class ClubCategory(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=6, unique=True)

    def __unicode__(self):
        return self.name

class Club(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(ClubCategory, related_name='clubs')
    logo = models.ImageField(upload_to='logos', max_length=32)
    website = models.URLField(max_length=40, unique=True)

    def __unicode__(self):
        return self.name