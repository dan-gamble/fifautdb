# Core imports
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

# Local imports
from apps.core.cbv_mixins import CoreDetailMixin, CoreDetailFilteredMixin
from .models import Nation


class NationListView(ListView):
    # Define the model for the CBV
    model = Nation
    # 50 'nations' per page
    paginate_by = 50

    def get_queryset(self):
        queryset = Nation.objects.all().prefetch_related('leagues')
        return queryset


class NationDetailView(CoreDetailMixin, DetailView):
    # The template to use
    model = Nation


class NationDetailFilteredView(CoreDetailFilteredMixin, DetailView):
    # The template to use
    model = Nation