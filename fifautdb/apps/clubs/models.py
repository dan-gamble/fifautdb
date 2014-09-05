# Core imports
from django.db import models
from django.utils.functional import cached_property

# Local imports
from players.models import Player


class Club(models.Model):
    id = models.IntegerField(
        primary_key=True
    )
    asset_id = models.IntegerField(
        unique=True
    )
    name = models.CharField(
        max_length=100
    )
    name_abbr3 = models.CharField(
        max_length=5
    )
    name_abbr7 = models.CharField(
        max_length=10
    )
    name_abbr15 = models.CharField(
        max_length=20
    )
    league = models.ForeignKey(
        'leagues.League',
        to_field='asset_id',
        related_name='clubs'
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
        max_length=50,
        blank=True
    )

    @models.permalink
    def get_absolute_url(self):
        return 'clubs:club', (), {
            'slug': self.slug
        }

    class Meta:
        db_table = 'clubs_14'

    def __unicode__(self):
        return '(' + self.name_abbr3 + ') ' + self.name_abbr15

    def get_class_name(self):
        return self.__class__.__name__

    @cached_property
    def count_players(self):
        return Player.objects.filter(club_id=self.asset_id).count()

    @cached_property
    def count_players_bronze(self):
        return Player.objects.filter(
            club_id=self.asset_id,
            overall_rating__lte=64
        ).exclude(
            card_type__gte=2
        ).count()

    @cached_property
    def count_players_silver(self):
        return Player.objects.filter(
            club_id=self.asset_id,
            overall_rating__range=(65, 74)
        ).exclude(
            card_type__gte=2
        ).count()

    @cached_property
    def count_players_gold(self):
        return Player.objects.filter(
            club_id=self.asset_id,
            overall_rating__gte=75
        ).exclude(
            card_type__gte=2
        ).count()

    def count_players_if(self):
        return Player.objects.filter(
            club_id=self.asset_id,
            card_type__gte=2
        ).count()

    def count_players_goalkeepers(self):
        return Player.objects.filter(
            club_id=self.asset_id,
            role_line=0
        ).count()

    def count_players_defenders(self):
        return Player.objects.filter(
            club_id=self.asset_id,
            role_line=1
        ).count()

    def count_players_midfielders(self):
        return Player.objects.filter(
            club_id=self.asset_id,
            role_line=2
        ).count()

    def count_players_forwards(self):
        return Player.objects.filter(
            club_id=self.asset_id,
            role_line=3
        ).count()

    @cached_property
    def players_average(self):
        return Player.objects.filter(
            club_id=self.asset_id,
        ).aggregate(
            models.Avg('overall_rating')
        ).values()[0]
