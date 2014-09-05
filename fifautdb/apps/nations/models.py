# Django
from django.db import models

# Local
from leagues.models import League


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
    slug = models.SlugField(
        max_length=50
    )
    name = models.CharField(
        max_length=100
    )
    name_abbr3 = models.CharField(
        max_length=3
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