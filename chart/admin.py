from django.contrib import admin

from content.admin import ModelBaseAdmin
from chart.models import Chart, ChartEntry, ChartOptions

'''
class ChartEntryAdmin(admin.ModelAdmin):
    list_display = ModelBaseAdmin.list_display + ('chart',)
    list_filter = ModelBaseAdmin.list_filter + ('chart',)
'''
admin.site.register(Chart, ModelBaseAdmin)
admin.site.register(ChartEntry)
admin.site.register(ChartOptions)