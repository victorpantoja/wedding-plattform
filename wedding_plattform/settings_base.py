import os
from functools import partial


get_path_to = partial(os.path.join, os.path.dirname(__file__))

DEBUG = False

TEMPLATE_PATH = get_path_to("templates")
STATIC_PATH = get_path_to("static")

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'NOTSET',
        'handlers': ['console'],
    },
    'formatters': {
        'detailed': {
            'format': '%(asctime)s %(levelname)s %(message)s',
        },
        'simple': {
            'format': '%(levelname)s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
}

MEMCACHE = {
    'servers': ('localhost:11211',),
    'socket_timeout': 1,
}
