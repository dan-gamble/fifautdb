# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nation',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('asset_id', models.IntegerField(unique=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('modified', models.DateTimeField(null=True, blank=True)),
                ('slug', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('name_abbr3', models.CharField(max_length=3)),
            ],
            options={
                'ordering': [b'name'],
                'db_table': b'nations_14',
            },
            bases=(models.Model,),
        ),
    ]
