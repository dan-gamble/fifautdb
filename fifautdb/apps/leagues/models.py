# Core imports
from django.db import models


class League(models.Model):
    id = models.IntegerField(
        primary_key=True
    )
    asset_id = models.IntegerField(
        unique=True
    )
    name = models.CharField(
        max_length=100
    )
    name_abbr5 = models.CharField(
        max_length=5
    )
    name_abbr15 = models.CharField(
        max_length=20
    )
    nation = models.ForeignKey(
        'nations.Nation',
        to_field='asset_id',
        related_name='leagues'
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

    players_count = models.IntegerField(
        blank=True,
        null=True
    )

    players_average_rating = models.IntegerField(
        blank=True,
        null=True
    )

    players_inform = models.IntegerField(
        blank=True,
        null=True
    )
    players_gold = models.IntegerField(
        blank=True,
        null=True
    )
    players_silver = models.IntegerField(
        blank=True,
        null=True
    )
    players_bronze = models.IntegerField(
        blank=True,
        null=True
    )

    players_gk = models.IntegerField(
        blank=True,
        null=True
    )
    players_def = models.IntegerField(
        blank=True,
        null=True
    )
    players_mid = models.IntegerField(
        blank=True,
        null=True
    )
    players_att = models.IntegerField(
        blank=True,
        null=True
    )


    @models.permalink
    def get_absolute_url(self):
        return 'leagues:league', (), {
            'slug': self.slug
        }

    class Meta:
        db_table = 'leagues_14'
        ordering = ['asset_id']

    def __unicode__(self):
        return '(' + self.name_abbr5 + ') ' + self.name_abbr15

    def get_class_name(self):
        return self.__class__.__name__