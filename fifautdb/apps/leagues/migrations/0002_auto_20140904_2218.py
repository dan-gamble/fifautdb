# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='league',
            name='nation',
            field=models.ForeignKey(related_name=b'leagues', to='nations.Nation', to_field=b'asset_id'),
        ),
    ]
