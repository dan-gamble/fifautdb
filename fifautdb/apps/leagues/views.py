# Core imports
from django.views.generic import DetailView, ListView

# Local imports
from core.cbv_mixins import DetailMixin, DetailFilteredMixin
from .models import League


class LeagueListView(ListView):
    # Define the model for the CBV
    model = League


class LeagueDetailView(DetailMixin, DetailView):
    # Define the model for the CBV
    model = League


class LeagueDetailFilteredView(DetailFilteredMixin, DetailView):
    # Define the model for the CBV
    model = League