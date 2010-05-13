from django.utils.translation import ugettext_lazy as _

import django_filters

from chart.models import ChartEntry

class RangeFilter(django_filters.Filter):
    
    def __init__(self, count, interval, *args, **kwargs):
        self.count = count
        self.interval = interval
        self.options = {
            '1, 10': (_('1-10'), lambda qs, name: qs.filter('%s___range=(1, 10)' % name)),
        }
        kwargs['choices'] = [(key, value[0]) for key, value in self.options.iteritems()]
        super(RangeFilter, self).__init__(*args, **kwargs)
        
        # {'1-10':  (('1-10'), lambda query}
        
        # Setup options.

class ChartFilterSet(django_filters.FilterSet):
    
    class Meta:
        model = ChartEntry
        fields = ['current_position']

    def __init__(self, data=None, queryset=None, prefix=None, action_url='', interval=10):
        self.current_position = RangeFilter(queryset.count(), interval)
        super(ChartFilterSet, self).__init__(data, queryset, prefix)
        
        


# Chart.objects.filter(chartentries__current_position__range=(1, 10))