from django import template

register = template.Library()

@register.inclusion_tag('chart/inclusion_tags/chart_list.html')
def chart_listing(object_list):
    return {'object_list': object_list}

@register.inclusion_tag('chart/inclusion_tags/chart_detail.html')
def chart_detail(obj):
    return {'object': obj}
