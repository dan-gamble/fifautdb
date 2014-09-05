# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='league',
            field=models.ForeignKey(related_name=b'clubs', to='leagues.League', to_field=b'asset_id'),
        ),
    ]
