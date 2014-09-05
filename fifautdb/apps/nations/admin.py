# Core
from django.contrib import admin

# Local
from .models import Nation


@admin.register(Nation)
class NationAdmin(admin.ModelAdmin):
    # fieldsets = (
    #     ('Nation options', {
    #         'fields': ('asset_id', 'name', 'name_abbr3')
    #     }),
    # )
    prepopulated_fields = {'slug': ('name', ), }