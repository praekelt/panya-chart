import django_filters

from content.filters import IntervalOrderFilterSet
from content.generic.views import GenericObjectDetail, GenericObjectList
from chart.models import Chart

class ObjectList(GenericObjectList):
    def get_extra_context(self, *args, **kwargs):
        extra_context = super(ObjectList, self).get_extra_context(*args, **kwargs)
        added_context = {'title': 'Charts'}
        if extra_context:
            extra_context.update(
                added_context,
            )
        else:
            extra_context = added_context

        return extra_context
    
    def get_filterset(self, request, queryset):
        return None
    
    def get_paginate_by(self):
        return 12
    
    def get_queryset(self):
        return Chart.permitted.all()

object_list = ObjectList()

class ObjectDetail(GenericObjectList):
    def get_queryset(self, slug):
        return Chart.permitted.get(slug=slug).chartentries.all().order_by('current_position')
    
    def get_extra_context(self, *args, **kwargs):
        extra_context = super(ObjectDetail, self).get_extra_context(*args, **kwargs)
        added_context = {'title': 'Chart'}
        if extra_context:
            extra_context.update(
                added_context,
            )
        else:
            extra_context = added_context
        return extra_context
    
    def get_filterset(self, request, queryset):
        return None
    
object_detail = ObjectDetail()
