from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'chart.views',
    url(r'^list/$', 'object_list', name='chart_object_list'),
    url(r'^(?P<slug>[\w-]+)/$', 'object_detail', name='chart_object_detail'),
)
