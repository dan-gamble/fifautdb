from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

from model_utils.models import TimeStampedModel
from fifautdb.apps.clubs.models import Club
from fifautdb.apps.leagues.models import League
from fifautdb.apps.nations.models import Nation
from fifautdb.apps.players.models import Player


class Profile(TimeStampedModel):
    user = models.OneToOneField(User)
    bio = models.TextField()
    slug = models.SlugField()

    fav_player = models.ForeignKey(Player)
    fav_club = models.ForeignKey(Club)
    fav_nation = models.ForeignKey(Nation)
    fav_league = models.ForeignKey(League)

    psn = models.CharField(max_length=50, unique=True)
    xbl = models.CharField(max_length=50, unique=True)
    origin = models.CharField(max_length=50, unique=True)

    twitter = models.CharField(max_length=50, unique=True)
    ea_forum = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile', args=[self.slug])