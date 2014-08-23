# Core imporst
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

# Local imports
from apps.core import views

urlpatterns = patterns(
    '',
    url(
        r'^$',
        views.index,
        name='index'
    ),
    # Admin URLS
    url(
        r'^admin/',
        include(admin.site.urls)
    ),
    # Clubs URLS
    url(
        r'^clubs/',
        include('apps.clubs.urls', namespace='clubs'),
    ),
    # Leagues URLS
    url(
        r'^leagues/',
        include('apps.leagues.urls', namespace='leagues'),
    ),
    # Nations URLS
    url(
        r'^nations/',
        include('apps.nations.urls', namespace='nations'),
    ),
    # Players URLS
    url(
        r'^players/',
        include('apps.players.urls', namespace='players'),
    ),
    # url(r'^/app/', include('apps.app.urls', namespace='app')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url("^404/$", TemplateView.as_view(template_name="404.html")),
        url("^500/$", TemplateView.as_view(template_name="500.html")),
    )
