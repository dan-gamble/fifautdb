# Core imports
from django.views.generic import ListView, DetailView

# Local imports
from apps.leagues.models import League
from apps.nations.models import Nation
from .models import Player


class PlayerListView(ListView):
    model = Player
    paginate_by = 50
    context_object_name = 'players'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PlayerListView, self).get_context_data(**kwargs)

        context['nations'] = Nation.objects.all()
        context['skill_moves'] = Player.objects.values('skill_moves').order_by('skill_moves').distinct('skill_moves')

        # Add kwargs as variables to the template
        context.update(self.kwargs)

        return context


class PlayerListFilteredView(ListView):
    model = Player
    paginate_by = 50
    context_object_name = 'players'

    def get_queryset(self):
        queryset = Player.objects.all()
        player_positions = {
            'att': 3,
            'mid': 2,
            'def': 1,
            'gk': 0
        }
        if self.kwargs['player_pos'] in player_positions:
            queryset = queryset.filter(
                role_line=player_positions[self.kwargs['player_pos']]
            )

        # Define the available card types
        card_types = {
            'if': {'card_type__gte': 2},
            'gold': {'overall_rating__gte': 75},
            'silver': {'overall_rating__range': (65, 74)},
            'bronze': {'overall_rating__lte': 64}
        }
        # Check if the given card type is in the dictionary because 'all' throws an KeyError
        if self.kwargs['card_type'] in card_types:
            queryset = queryset.filter(**card_types[self.kwargs['card_type']])

        # Don't show inform cards for specific colour card types
        if self.kwargs['card_type'] not in ['if', 'all']:
            queryset = queryset.exclude(card_type__gte=2)

        try:
            nations = Nation.objects.get(slug=self.kwargs['nation'])
            queryset = queryset.filter(
                nation_id=nations.asset_id
            )
        except Nation.DoesNotExist:
            pass

        try:
            leagues = League.objects.get(slug=self.kwargs['league'])
            queryset = queryset.filter(
                league_id=leagues.asset_id
            )
        except League.DoesNotExist:
            pass

        workrates = {
            'high': 2,
            'medium': 0,
            'low': 1
        }
        if self.kwargs['att_workrate'] in workrates:
            queryset = queryset.filter(
                att_workrate=workrates[self.kwargs['att_workrate']]
            )
        if self.kwargs['def_workrate'] in workrates:
            queryset = queryset.filter(
                def_workrate=workrates[self.kwargs['def_workrate']]
            )

        try:
            queryset = queryset.filter(
                skill_moves=self.kwargs['skill_move']
            )
        except ValueError:
            pass

        try:
            queryset = queryset.filter(
                weak_foot=self.kwargs['weak_foot']
            )
        except ValueError:
            pass

        # Define the available sort by keys
        sorts = {
            'ovr': 'overall_rating',
            'att1': 'card_att1',
            'att2': 'card_att2',
            'att3': 'card_att3',
            'att4': 'card_att4',
            'att5': 'card_att5',
            'att6': 'card_att6'
        }
        # Add a descending order to the existing queryset
        queryset = queryset.order_by('-' + sorts[self.kwargs['sort_by']])

        return queryset

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PlayerListFilteredView, self).get_context_data(**kwargs)

        context['nations'] = Nation.objects.all()
        context['skill_moves'] = Player.objects.values('skill_moves').order_by('skill_moves').distinct('skill_moves')

        # Add kwargs as variables to the template
        context.update(self.kwargs)

        return context


class PlayerDetailView(DetailView):
    # Define the model for the CBV
    model = Player