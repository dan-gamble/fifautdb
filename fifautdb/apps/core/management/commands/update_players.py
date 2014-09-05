#!/usr/bin/env python
# Django
from django.core.management.base import BaseCommand
from django.db import models

# Local
from nations.models import Nation
from players.models import Player
# from core.functions import cbv_pagination, base_objects_add_id, base_objects


class Command(BaseCommand):

    def handle(self, *args, **options):

        # for arg in args:
        #     try:
        for nation in Nation.objects.all():

            nation.players_count = Player.objects.filter(
                nation_id=nation.asset_id
            ).count()

            nation.players_inform = Player.objects.filter(
                nation_id=nation.asset_id,
                card_type__gte=2
            ).count()

            nation.players_gold = Player.objects.filter(
                nation_id=nation.asset_id,
                overall_rating__gte=75
            ).exclude(
                card_type__gte=2
            ).count()

            nation.players_silver = Player.objects.filter(
                nation_id=nation.asset_id,
                overall_rating__range=(65, 74)
            ).exclude(
                card_type__gte=2
            ).count()

            nation.players_bronze = Player.objects.filter(
                nation_id=nation.asset_id,
                overall_rating__lte=64
            ).exclude(
                card_type__gte=2
            ).count()

            nation.players_average_rating = Player.objects.filter(
                nation_id=nation.asset_id,
            ).aggregate(
                models.Avg('overall_rating')
            ).values()[0]

            print nation

            nation.save()
