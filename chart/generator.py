import random

from generate import IMAGES
from generate.json_loader import load_json
from music.generator import generate as music_generator

CHART_COUNT = 1
CHART_ENTRY_COUNT = 40

def generate():
    objects = []
    
    # gen chart entry objects
    for i in range(1, CHART_ENTRY_COUNT + 1):
        
        
        if i > 20:
            music_count = i - 20
        else:
            music_count = i
        
        objects.append({
            "model": "chart.ChartEntry",
            "fields": {
                "previous_position": random.randint(0, 40),
                "current_position": i,
                "next_position": random.randint(0, 40),
                "remove": False,
                "chart": {
                    "model": "chart.Chart",
                    "fields": {
                        "title": "Chart 1 Title",
                        "state": "published",
                        "image": random.sample(IMAGES, 1)[0],
                        "sites": {
                            "model": "sites.Site",
                            "fields": { 
                                "name": "example.com"
                            }
                        },
                    }
                },
                "track": {
                    "model": "music.Track",
                    "fields": {
                        "title": "Track %s Title" % music_count,
                    }
                },
            },
        })
    
    load_json(objects)
