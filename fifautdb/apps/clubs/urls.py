# Core imports
from django.conf.urls import patterns, url

# Local imports
from .views import ClubListView, ClubDetailView, ClubDetailFilteredView

urlpatterns = patterns('',
                       url(
                           r'^$',
                           ClubListView.as_view(),
                           name='index'
                       ),
                       url(
                           r'^(?P<slug>[a-z0-9-]*)/$',
                           ClubDetailView.as_view(),
                           name='club'
                       ),
                       url(
                           r'^(?P<slug>[a-z0-9-]*)/'
                           r'(?P<card_type>[a-z]*)/'
                           r'(?P<role_line>[a-z]*)/'
                           r'(?P<sort_by>[a-z0-9]*)/$',
                           ClubDetailFilteredView.as_view(),
                           name='club_filter'
                       ),
                       )
