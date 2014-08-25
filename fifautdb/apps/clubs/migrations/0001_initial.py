# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('asset_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('name_abbr3', models.CharField(max_length=5)),
                ('name_abbr7', models.CharField(max_length=10)),
                ('name_abbr15', models.CharField(max_length=20)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('modified', models.DateTimeField(null=True, blank=True)),
                ('slug', models.CharField(max_length=50, blank=True)),
                ('league', models.ForeignKey(to='leagues.League', to_field=b'asset_id')),
            ],
            options={
                'db_table': b'clubs_14',
            },
            bases=(models.Model,),
        ),
    ]
