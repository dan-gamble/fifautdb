# Core imports
from django.conf.urls import patterns, url

# Local imports
from .views import PlayerListView, PlayerListFilteredView, PlayerDetailView

urlpatterns = patterns('',
                       url(
                           r'^$',
                           PlayerListView.as_view(),
                           name='index'
                       ),
                       url(
                           r'^(?P<player_pos>[a-z]*)/'
                           r'(?P<card_type>[a-z]*)/'
                           r'(?P<nation>[a-z-]*)/'
                           r'(?P<league>[a-z0-9-]*)/'
                           r'(?P<att_workrate>[a-z]*)/'
                           r'(?P<def_workrate>[a-z]*)/'
                           r'(?P<skill_move>[a-z0-9]*)/'
                           r'(?P<weak_foot>[a-z0-9]*)/'
                           r'(?P<sort_by>[a-z0-9]*)/$',
                           PlayerListFilteredView.as_view(),
                           name='index_filter'
                       ),
                       url(
                           r'^(?P<slug>[a-z0-9-]*)/$',
                           PlayerDetailView.as_view(),
                           name='player'
                       ),
                       )
