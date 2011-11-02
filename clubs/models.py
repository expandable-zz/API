# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class ClubCategory(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)

class Club(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(ClubCategory, related_name='category_set')
    logo = models.ImageField(upload_to='logos', max_length=20)
    website = models.CharField(max_length=40, unique=True)
    api_key = models.CharField(max_length=40, unique=True)