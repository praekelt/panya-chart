from django.core.management.base import BaseCommand

from chart.models import Chart

class Command(BaseCommand):
    def handle(self, *app_labels, **options):
        object_list = Chart.object.all()
        for entry in object_list.chartentries:
            if entry.remove:
                entry.delete()
            else:
                entry.previous_position = entry.current_position
                entry.current_position = entry.next_position
                entry.next_position = 0
                entry.save()
