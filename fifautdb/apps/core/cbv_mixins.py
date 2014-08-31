# Core imports
from django.db.models import Q
from collections import OrderedDict

# Local imports
from core.functions import cbv_pagination, base_objects
from players.models import Player


class FilterLabels(object):

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(FilterLabels, self).get_context_data(**kwargs)

        # Ordered Dictionaries created for the 'controls' in the Object
        # templates

        # Card types
        context['card_type_labels'] = OrderedDict([
            ('all', 'All'),
            ('gold', 'Gold'),
            ('silver', 'Silver'),
            ('bronze', 'Bronze')
        ])
        # Roles
        context['role_labels'] = OrderedDict([
            ('all', 'All'),
            ('att', 'Attackers'),
            ('mid', 'Midfielders'),
            ('def', 'Defenders'),
            ('gk', 'Goalkeepers')
        ])
        # Sorts (Different labels if role === 'gk')
        context['sort_labels_gk'] = OrderedDict([
            ('ovr', 'Overall'),
            ('att1', 'Diving'),
            ('att2', 'Handling'),
            ('att3', 'Kicking'),
            ('att4', 'Reflexes'),
            ('att5', 'Speed'),
            ('att6', 'Positioning')
        ])
        context['sort_labels_else'] = OrderedDict([
            ('ovr', 'Overall'),
            ('att1', 'Pace'),
            ('att2', 'Shooting'),
            ('att3', 'Passing'),
            ('att4', 'Dribbling'),
            ('att5', 'Defending'),
            ('att6', 'Heading')
        ])

        return context


class DetailMixin(FilterLabels):

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DetailMixin, self).get_context_data(**kwargs)

        # Pull all the players that belong to the object_type
        player_list = Player.objects.filter(
            **{base_objects(context): context['object'].asset_id}
        ).select_related(
            'club',
            'league',
            'nation'
        )

        # Create pagination
        cbv_pagination(self, context, player_list, 28, 'players')

        return context


class DetailFilteredMixin(FilterLabels):

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DetailFilteredMixin, self).get_context_data(**kwargs)

        # Create the base queryset for which we filter on
        context['players'] = Player.objects.filter(
            **{base_objects(context): context['object'].asset_id}
        ).select_related(
            'club',
            'league',
            'nation'
        )

        # Dictionaries to check kwargs against to created queryset filters
        # Card types
        card_types = {
            'inform': {'card_type__gte': 2},
            'gold': {'overall_rating__gte': 75},
            'silver': {'overall_rating__range': (65, 74)},
            'bronze': {'overall_rating__lte': 64}
        }
        # Roles
        role_lines = {
            'att': 3,
            'mid': 2,
            'def': 1,
            'gk': 0
        }
        # Sorts
        sorts = {
            'ovr': 'overall_rating',
            'att1': 'card_att1',
            'att2': 'card_att2',
            'att3': 'card_att3',
            'att4': 'card_att4',
            'att5': 'card_att5',
            'att6': 'card_att6'
        }

        # Check kwargs against created dictionaries to create filters
        # Card types
        if self.kwargs['card_type'] in card_types:
            context['players'] = context['players'].filter(
                **card_types[self.kwargs['card_type']]
            )
        # Don't show inform cards for specific colour card types
        if self.kwargs['card_type'] not in ['inform', 'all']:
            context['players'] = context['players'].exclude(card_type__gte=2)
        # Roles
        role_list = []
        if self.kwargs['role_line'] != 'all':
            for role in self.kwargs['role_line'].split('-'):
                role_list.append(role)
        # Create a Q Object for each role so we can have multiple roles selected
        q_objects = Q()
        for role in role_list:
            q_objects |= Q(role_line=role_lines[role])
        # Finally filter the queryset based on our work so far
        context['players'] = context['players'].filter(
            q_objects
        )
        # Sorts
        # Don't need to do any work as we are just ordering the already created
        # queryset
        context['players'] = context['players'].order_by(
            '-' + sorts[self.kwargs['sort_by']]
        )

        # Create the selected labels
        # Roles
        if role_list:
            context['role_label'] = []
            for role in role_list:
                if role in context['role_labels']:
                    context['role_label'].append(
                        context['role_labels'][role]
                    )
        elif not role_list:
            context['role_label'] = 'All'
        # Sorts
        if self.kwargs['role_line'] == 'gk':
            context['sort_label'] = context['sort_labels_gk'][self.kwargs['sort_by']]
        else:
            context['sort_label'] = context['sort_labels_else'][self.kwargs['sort_by']]

        # Create pagination on our 'players' queryset
        cbv_pagination(self, context, context['players'], 28, 'players')

        # Add kwargs as variables to the template
        context.update(self.kwargs)

        return context