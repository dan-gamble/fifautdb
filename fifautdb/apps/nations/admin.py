# Core imports
from django.contrib import admin

# Local imports
from .models import Nation


class NationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }

admin.site.register(Nation, NationAdmin)