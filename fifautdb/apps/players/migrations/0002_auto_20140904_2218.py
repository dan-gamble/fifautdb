# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='club',
            field=models.ForeignKey(related_name=b'players', to_field=b'asset_id', blank=True, to='clubs.Club', null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='league',
            field=models.ForeignKey(related_name=b'players', to_field=b'asset_id', blank=True, to='leagues.League', null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='nation',
            field=models.ForeignKey(related_name=b'players', to_field=b'asset_id', blank=True, to='nations.Nation', null=True),
        ),
    ]
