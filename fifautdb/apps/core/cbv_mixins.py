# Local imports
from django.db.models import Q
from core.functions import cbv_pagination
from players.models import Player


def base_objects(context):
    global filters
    # Define the available object types
    object_types = {
        'Club': 'club',
        'League': 'league',
        'Nation': 'nation'
    }
    # Gets the Object Type from the passed model and defines the base filter
    filters = object_types[context['object'].__class__.__name__] + '_id'
    return filters


class CoreDetailMixin(object):

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CoreDetailMixin, self).get_context_data(**kwargs)

        base_objects(context)
        # Pull all the players that belong to the object_type
        player_list = Player.objects.filter(
            **{filters: context['object'].asset_id}
        ).select_related('club', 'league', 'nation')

        # Create pagination
        cbv_pagination(self, context, player_list, 28, 'players')

        return context


class CoreDetailFilteredMixin(object):

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(
            CoreDetailFilteredMixin, self
        ).get_context_data(
            **kwargs
        )

        base_objects(context)
        # Pull all the players that belong to the object_type
        context['players'] = Player.objects.filter(
            **{filters: context['object'].asset_id}
        ).select_related('club', 'league', 'nation')

        # Define the available card types
        card_types = {
            'inform': {'card_type__gte': 2},
            'gold': {'overall_rating__gte': 75},
            'silver': {'overall_rating__range': (65, 74)},
            'bronze': {'overall_rating__lte': 64}
        }
        # Check if the given card type is in the dictionary because 'all'
        # throws an KeyError
        if self.kwargs['card_type'] in card_types:
            context['players'] = context['players'].filter(
                **card_types[self.kwargs['card_type']]
            )

        # Don't show inform cards for specific colour card types
        if self.kwargs['card_type'] not in ['inform', 'all']:
            context['players'] = context['players'].exclude(card_type__gte=2)

        # Define available role lines
        role_lines = {
            'att': 3,
            'mid': 2,
            'def': 1,
            'gk': 0
        }

        output = []

        for role in self.kwargs['role_line'].split('-'):
            output.append(role)

        print output

        # Check if the given role line is in the dictionary because 'all'
        # throws an KeyError
        # for role in output:
        #     if role in role_lines:
        #         context['players'] = context['players'].filter(
        #             role_line=role_lines[role]
        #         )
        #         print role
        #         print context['players']

        # Todo: Can't use output[0], [1] ofc.. Sort this shit out.
        q_objects = Q()
        for role in output:
            q_objects |= Q(role_line=role_lines[role])

        context['players'] = context['players'].filter(
            q_objects
        )
        print context['players']

        role_labels = {
            'all': 'All',
            'att': 'Attackers',
            'mid': 'Midfielders',
            'def': 'Defenders',
            'gk': 'Goalkeepers',
        }

        context['role_label'] = []
        for role in output:
            if role in role_labels:
                context['role_label'].append(role_labels[role])

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
        context['players'] = context['players'].order_by(
            '-' + sorts[self.kwargs['sort_by']]
        )

        sort_labels = {
            'gk': {
                'ovr': 'Overall',
                'att1': 'Diving',
                'att2': 'Handling',
                'att3': 'Kicking',
                'att4': 'Reflexes',
                'att5': 'Speed',
                'att6': 'Positioning'
            },
            'else': {
                'ovr': 'Overall',
                'att1': 'Pace',
                'att2': 'Shooting',
                'att3': 'Passing',
                'att4': 'Dribbling',
                'att5': 'Defending',
                'att6': 'Heading'
            }
        }

        if self.kwargs['role_line'] == 'gk':
            context['sort_label'] = sort_labels['gk'][self.kwargs['sort_by']]
        else:
            context['sort_label'] = sort_labels['else'][self.kwargs['sort_by']]

        # Create pagination
        cbv_pagination(self, context, context['players'], 28, 'players')

        # Add kwargs as variables to the template
        context.update(self.kwargs)

        return context