# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse
from django.utils.datetime_safe import datetime
from clubs.models import Club, ClubCategory
from users.models import User, ClassGroup
from system.models import Application,Session,Permission,Rank

def home(request):
    print User.objects.get(id=1).has_authorization(name = 'permission.delete',club=Club.objects.get(name='HIFI'))



    return HttpResponse("Bitch Nigga.")

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
        email='jarasson@efrei.fr')
    user.save()
    app=Application(name='Pouet',slug='pouet',api_key='1234',club=club)
    app.save()

    session=Session(token='2345', time_start=datetime.now(), time_end=datetime(2011,12,25),user=user,application=app)
    session.save()

    p1=Permission(name='permission.get')
    p2=Permission(name='permission.new')
    p3=Permission(name='global.permission.delete')
    p1.save()
    p2.save()
    p3.save()

    app.permissions.add(p1)
    app.permissions.add(p3)
    rank=Rank(name='Président')
    rank.save()
    rank.permissions.add(p1)
    rank.permissions.add(p3)
    rank.save()

    user.groups.create(rank=rank,club=club)


    return HttpResponse("Initialization." )