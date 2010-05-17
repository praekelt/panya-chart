from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'chart.views',
    url(r'^(?P<slug>[\w-]+)/$', 'object_detail', name='chart_object_detail'),
)
