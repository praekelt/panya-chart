from django.core.urlresolvers import reverse
from django.db import models

from content.models import ModelBase


class Chart(ModelBase):
    class Meta:
        verbose_name = 'Chart'
        verbose_name_plural = 'Charts'
    
    def get_absolute_url(self):
        return reverse('chart_object_detail', kwargs={'slug': self.slug})

class ChartEntry(ModelBase):
    chart = models.ForeignKey(
        Chart, 
        related_name='chartentries'
    )
    # TODO: add radio.models.Song foreign key to model
    current_position = models.IntegerField()
    previous_position = models.IntegerField()
    
    class Meta:
        verbose_name = 'Chart Entry'
        verbose_name_plural = 'Chart Entries'
        ordering = ['current_position']
    
    def position_difference(self):
        return str(self.current_position - self.position_difference)

    def __unicode__(self):
        return '%s entry %s' % (self.chart.title, self.current_position)
    