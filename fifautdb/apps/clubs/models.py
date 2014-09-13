from django.core.urlresolvers import reverse
from django.db import models


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

    def get_absolute_url(self):
        return reverse('club', args=[self.slug])

    class Meta:
        db_table = 'clubs_14'

    def __unicode__(self):
        return '(' + self.name_abbr3 + ') ' + self.name_abbr15

    def get_class_name(self):
        return self.__class__.__name__