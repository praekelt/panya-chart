from datetime import datetime

from django.core.urlresolvers import reverse
from django.db import models

from panya.models import ModelBase
from music.models import Track
from options.models import Options

class Chart(ModelBase):
    class Meta:
        verbose_name = 'Chart'
        verbose_name_plural = 'Charts'
    
    def get_absolute_url(self):
        return reverse('chart_object_detail', kwargs={'slug': self.slug})
        
    def __unicode__(self):
        return self.title

class ChartEntry(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    chart = models.ForeignKey(
        Chart, 
        related_name='chartentries'
    )
    track = models.ForeignKey(Track)
    previous_position = models.IntegerField(
        blank=True,
        null=True
    )
    current_position = models.IntegerField(
        blank=True,
        null=True
    )
    next_position = models.IntegerField(
        blank=True,
        null=True
    )
    remove = models.BooleanField(
        help_text="On the next update this entry will be removed completely."
    )
    
    class Meta:
        verbose_name = 'Chart entry'
        verbose_name_plural = 'Chart entries'
        ordering = ['current_position']
    
    def get_duration_on_chart(self):
        return datetime.now() - (datetime.now() - self.created)
    
    def __unicode__(self):
        return '%s Entry %s' % (self.chart.title, self.current_position)
        
class ChartOptions(Options):
    __module__ = 'options.models'

    primary_chart = models.ForeignKey(
        'chart.Chart',
        null=True,
        help_text="Select the primary chart link from the navigation.",
        related_name='chartoptions_primary_chart',
        limit_choices_to = {'state': 'published'}
    )
    
    class Meta:
        verbose_name = 'Chart options'
        verbose_name_plural = 'Chart options'
