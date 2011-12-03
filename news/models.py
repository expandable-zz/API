# -*- coding: utf-8 -*-
from django.db import models
from publications.models import Publication, Tag
from clubs.models import Club

# Create your models here.
class News(Publication):
    club = models.ForeignKey(Club, related_name='news')
    content = models.TextField(blank=True)

    def __unicode__(self):
        return self.title