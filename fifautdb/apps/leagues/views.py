# Core imports
from django.views.generic import DetailView, ListView

# Local imports
from apps.core.cbv_mixins import CoreDetailMixin, CoreDetailFilteredMixin
from .models import League


class LeagueListView(ListView):
    # Define the model for the CBV
    model = League


class LeagueDetailView(CoreDetailMixin, DetailView):
    # Define the model for the CBV
    model = League


class LeagueDetailFilteredView(CoreDetailFilteredMixin, DetailView):
    # Define the model for the CBV
    model = League