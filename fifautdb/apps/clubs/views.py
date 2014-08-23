# Core imports
from django.views.generic import ListView, DetailView

# Local imports
from apps.core.cbv_mixins import CoreDetailMixin, CoreDetailFilteredMixin
from .models import Club


class ClubListView(ListView):
    # Define the model for the CBV
    model = Club
    # Set the number of clubs per page
    paginate_by = 50


class ClubDetailView(CoreDetailMixin, DetailView):
    # Define the model for the CBV
    model = Club


class ClubDetailFilteredView(CoreDetailFilteredMixin, DetailView):
    # Define the model for the CBV
    model = Club