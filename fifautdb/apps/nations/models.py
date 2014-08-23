# Core imports
from django.db import models

# Local imports
from django.db.models import Avg
from apps.leagues.models import League
from apps.players.models import Player


class Nation(models.Model):
    id = models.IntegerField(
        primary_key=True
    )
    asset_id = models.IntegerField(
        unique=True
    )
    created = models.DateTimeField(
        blank=True,
        null=True
    )
    modified = models.DateTimeField(
        blank=True,
        null=True
    )
    slug = models.CharField(
        max_length=50
    )
    name = models.CharField(
        max_length=100
    )
    name_abbr3 = models.CharField(
        max_length=3
    )

    @models.permalink
    def get_absolute_url(self):
        return 'nations:nation', (), {
            'slug': self.slug
        }

    class Meta:
        db_table = 'nations_14'
        ordering = ['name']

    def __unicode__(self):
        return '(' + self.name_abbr3 + ') ' + self.name

    def get_class_name(self):
        return self.__class__.__name__

    def leagues(self):
        return League.objects.filter(nation=self.asset_id)

    def players(self):
        return Player.objects.filter(nation_id=self.asset_id)

    def players_bronze(self):
        return Player.objects.filter(
            nation_id=self.asset_id,
            overall_rating__lte=64
        ).exclude(
            card_type__gte=2
        )

    def players_silver(self):
        return Player.objects.filter(
            nation_id=self.asset_id,
            overall_rating__range=(65, 74)
        ).exclude(
            card_type__gte=2
        )

    def players_gold(self):
        return Player.objects.filter(
            nation_id=self.asset_id,
            overall_rating__gte=75
        ).exclude(
            card_type__gte=2
        )

    def players_if(self):
        return Player.objects.filter(
            nation_id=self.asset_id,
            card_type__gte=2
        )

    def players_goalkeepers(self):
        return Player.objects.filter(
            nation_id=self.asset_id,
            role_line=0
        )

    def players_defenders(self):
        return Player.objects.filter(
            nation_id=self.asset_id,
            role_line=1
        )

    def players_midfielders(self):
        return Player.objects.filter(
            nation_id=self.asset_id,
            role_line=2
        )

    def players_forwards(self):
        return Player.objects.filter(
            nation_id=self.asset_id,
            role_line=3
        )

    def players_average(self):
        return Player.objects.filter(
            nation_id=self.asset_id,
            ).aggregate(
            Avg('overall_rating')
        ).values()[0]