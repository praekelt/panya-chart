import django_filters

from chart.models import ChartEntry

class ChartRangeFilter(django_filters.FilterSet):
    class Meta:
        model = ChartEntry
        fields = ['price', 'release_date']
