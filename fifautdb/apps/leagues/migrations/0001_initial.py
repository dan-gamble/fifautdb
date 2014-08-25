# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('asset_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('name_abbr5', models.CharField(max_length=5)),
                ('name_abbr15', models.CharField(max_length=20)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('modified', models.DateTimeField(null=True, blank=True)),
                ('slug', models.CharField(max_length=50)),
                ('nation', models.ForeignKey(to='nations.Nation', to_field=b'asset_id')),
            ],
            options={
                'ordering': [b'asset_id'],
                'db_table': b'leagues_14',
            },
            bases=(models.Model,),
        ),
    ]
