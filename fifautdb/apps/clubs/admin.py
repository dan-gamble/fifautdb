# Core imports
from django.contrib import admin

# Local imports
from .models import Club


class ClubAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }

admin.site.register(Club, ClubAdmin)