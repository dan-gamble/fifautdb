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
        to_field='asset_id'
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