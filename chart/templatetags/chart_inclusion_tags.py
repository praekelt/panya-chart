from django import template

register = template.Library()

@register.inclusion_tag('chart/inclusion_tags/chartentry_listing.html')
def chartentry_listing(object_list):
    return {'object_list': object_list}
