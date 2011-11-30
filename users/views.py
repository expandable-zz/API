# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse
from django.utils.datetime_safe import datetime
from clubs.models import Club, ClubCategory
from users.models import User, ClassGroup
from system.models import Application,Session

def home(request):

    return HttpResponse("Bitch Nigga." )

def init(request):

    club_category = ClubCategory(name='Techno')
    club_category.save()
    club = Club(name='HIFI', category= club_category)
    club.save()
    class_group=ClassGroup(label='L3')
    class_group.save()
    user = User(first_name='Rémi',
        last_name='Jarasson',
        username='jarasson',
        birthdate=datetime(1991,01,17),
        email='jarasson@efrei.fr',
        leaving_year=2014,
        class_group=class_group)
    user.save()
    app=Application(name='Pouet',slug='pouet',api_key='1234',club=club)
    app.save()
    session=Session(token='2345', time_start=datetime.now(), time_end=datetime(2011,12,25),user=user,app=app)
    session.save()


    return HttpResponse("Initialization." )