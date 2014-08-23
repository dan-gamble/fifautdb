# Core imports
from django.contrib import admin

# Local imports
from .models import Player


class PlayerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('common_name',), }

admin.site.register(Player, PlayerAdmin)