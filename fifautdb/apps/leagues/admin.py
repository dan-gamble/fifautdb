# Core imports
from django.contrib import admin

# Local imports
from .models import League


class LeagueAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', ), }

admin.site.register(League, LeagueAdmin)
