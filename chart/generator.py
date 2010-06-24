import random

from generate import IMAGES
from generate.json_loader import load_json

CHART_COUNT = 1
CHART_ENTRY_COUNT = 40
CREDIT_COUNT = 40
TRACK_COUNT = 20

CONTRIBUTOR_ROLE = [[1, "Artist"], [2, "Producer"], [3, "Composer"]]

def generate():
    objects = []
    
    # generate chart track objects
    for i in range(1, CREDIT_COUNT + 1):
        contributor_role = random.choice(CONTRIBUTOR_ROLE)
        objects.append({
            "model": "music.Credit",
            "fields": {
                "role": contributor_role[0],
                "track": {
                    "model": "music.Track",
                    "fields": {
                        "title": "Chart Track %s Title" % i,
                        "description": "Chart Track %s description with some added text to verify truncates where needed." % i,
                        "state": "published",
                        "image": random.sample(IMAGES, 1)[0],
                        "video_embed": "",
                        "sites": {
                            "model": "sites.Site",
                            "fields": { 
                                "name": "example.com"
                            }
                        },
                        "album": {
                            "model": "music.Album",
                            "fields": {
                                "title": "Chart Album %s Title" % i,
                                "description": "Chart Album %s description with some added text to verify truncates where needed." % i,
                                "state": "published",
                                "image": random.sample(IMAGES, 1)[0],
                                "sites": {
                                    "model": "sites.Site",
                                    "fields": { 
                                        "name": "example.com"
                                    }
                                },
                            },
                        },
                    },
                },
                "contributor": {
                    "model": "music.TrackContributor",
                    "fields": {
                        "title": "Chart Track Contributor %s Title" % i,
                        "description": "Chart Track Contributor %s description with some added text to verify truncates where needed." % i,
                        "state": "published",
                        "image": random.sample(IMAGES, 1)[0],
                        "sites": {
                            "model": "sites.Site",
                            "fields": { 
                                "name": "example.com"
                            }
                        },
                    },
                },
            },
        })
    
    # gen chart entry objects
    for i in range(1, CHART_ENTRY_COUNT + 1):
        
        objects.append({
            "model": "chart.ChartEntry",
            "fields": {
                "previous_position": random.randint(1, 40),
                "current_position": i,
                "next_position": random.randint(1, 40),
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
                        "title": "Chart Track %s Title" % i,
                    }
                },
            },
        })
    
    # create chart options
    objects.append({
        "model": "preferences.ChartPreferences",
        "fields": {
            "primary_chart": {
                "model": "chart.Chart",
                "fields": {
                    "title": "Chart 1 Title",
                }
            },
        }
    })
    
    load_json(objects)
