# Django
from django.core.management.base import BaseCommand
from django.db import models
from django.db.models.loading import get_model

# Local
from players.models import Player


class Command(BaseCommand):

    def handle(self, *args, **options):

        for arg in args:

            '''
            Create the lower case model name and the column on
            the player table which we filter on
            '''
            object_types = {
                'Clubs': {
                    'name': 'club',
                    'id': 'club_id'
                },
                'Leagues': {
                    'name': 'league',
                    'id': 'league_id'
                },
                'Nations': {
                    'name': 'nation',
                    'id': 'nation_id'
                }
            }

            # Get the model from the passed argument
            model = get_model(arg.lower(), object_types[arg]['name'])

            for model_object in model.objects.all():

                queryset = Player.objects.filter(
                    **{object_types[arg]['id']: model_object.asset_id}
                )

                # Create the base queryset we will filter on
                model_object.players_count = queryset.count()

                model_object.players_inform = queryset.filter(
                    card_type__gte=2
                ).count()

                model_object.players_gold = queryset.filter(
                    overall_rating__gte=75
                ).exclude(
                    card_type__gte=2
                ).count()

                model_object.players_silver = queryset.filter(
                    overall_rating__range=(65, 74)
                ).exclude(
                    card_type__gte=2
                ).count()

                model_object.players_bronze = queryset.filter(
                    overall_rating__lte=64
                ).exclude(
                    card_type__gte=2
                ).count()

                model_object.players_average_rating = list(queryset.aggregate(
                    models.Avg('overall_rating')
                ).values())[0]

                print(model_object.players_average_rating)

                model_object.save()
            else:
                print('All models updated :)')