from django.contrib import admin

from content.admin import ModelBaseAdmin
from chart.models import Chart, ChartEntry, ChartOptions


class ChartEntryAdmin(admin.ModelAdmin):
    list_display = ('chart', 'track', 'current_position', 'remove')
    list_filter = ('chart', 'created')
    search_fields = ('created',)

admin.site.register(Chart, ModelBaseAdmin)
admin.site.register(ChartEntry, ChartEntryAdmin)
admin.site.register(ChartOptions)
