Django Chart:
=============
**Django radio chart app.**


Dependancies:
=============
django-content
    git@github.com:praekelt/django-content.git


Models:
=======

Chart:
------
class models.Chart
    
Chart model extends content.models.ModelBase. Add chart to the CMS and link related chart entries via foreign key.

API Reference:
~~~~~~~~~~~~~~

FIELDS
******
extends django-content fields
    See django-content README

METHODS
*******
get_absolute_url::
    Chart.get_absolute_url()
Calculate the URL for the chart object

MANAGERS
********
None

ChartEntry:
-----------
class models.ChartEntry
    
ChartEntry model extends content.models.ModelBase. Add chart entries to CMS and link to a Chart object via a foreign key.

API Reference:
~~~~~~~~~~~~~~

FIELDS
******
chart
    Foreign key to chart object.
current_position
    Current entries position on the chart.
previous_position
    Entries previous position on the chart.
extends django-content fields
    See django-content README

METHODS
*******
position_difference::
    ChartEntry.position_difference()
Calculate how many places the entry has dropped or risen on the chart.

MANAGERS
********
None


Tag Reference
=============

Inclusion Tags
--------------
None

Template Tags
-------------
None
