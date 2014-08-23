# Core imports
from django.conf.urls import patterns, url

# Local imports
from .views import LeagueListView, LeagueDetailView, LeagueDetailFilteredView

urlpatterns = patterns('',
                       url(
                           r'^$',
                           LeagueListView.as_view(),
                           name='index'
                       ),
                       url(
                           r'^(?P<slug>[a-z0-9-]*)/$',
                           LeagueDetailView.as_view(),
                           name='league'
                       ),
                       url(
                           r'^(?P<slug>[a-z0-9-]*)/'
                           r'(?P<card_type>[a-z]*)/'
                           r'(?P<role_line>[a-z]*)/'
                           r'(?P<sort_by>[a-z0-9]*)/$',
                           LeagueDetailFilteredView.as_view(),
                           name='league_filter'
                       ),
                       )
