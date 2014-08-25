# Core imports
from django.conf.urls import patterns, url

# Local imports
from .views import NationListView, NationDetailView, NationDetailFilteredView

urlpatterns = patterns('',
                       url(
                           r'^$',
                           NationListView.as_view(),
                           name='list'
                       ),
                       url(
                           r'^(?P<slug>[a-z-]*)/$',
                           NationDetailView.as_view(),
                           name='nation'
                       ),
                       url(
                           r'^(?P<slug>[a-z-]*)/'
                           r'(?P<card_type>[a-z]*)/'
                           r'(?P<role_line>[a-z]*)/'
                           r'(?P<sort_by>[a-z0-9]*)/$',
                           NationDetailFilteredView.as_view(),
                           name='nation_filter'
                       ),
                       )
