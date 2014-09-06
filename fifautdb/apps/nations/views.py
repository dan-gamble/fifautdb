# Core imports
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

# Local imports
from core.cbv_mixins import DetailMixin, DetailFilteredMixin
from .models import Nation


class NationListView(ListView):
    # Define the model for the CBV
    model = Nation
    # 50 'nations' per page
    paginate_by = 50

    def get_queryset(self):
        queryset = Nation.objects.all().prefetch_related(
            'leagues'
        ).exclude(
            players_count__exact=0
        ).order_by(
            '-players_count'
        )
        return queryset


class NationDetailView(DetailMixin, DetailView):
    # The template to use
    model = Nation


class NationDetailFilteredView(DetailFilteredMixin, DetailView):
    # The template to use
    model = Nation