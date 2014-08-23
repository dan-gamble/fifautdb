# Core imports
from django.http import HttpResponse
from django.shortcuts import render

# Local imports
from apps.clubs.models import Club


def index(request):
    latest_clubs = Club.objects.order_by('-created')[0:5]

    return render(
        request,
        'core/index.html',
        {'latest_clubs': latest_clubs}
    )