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

AWS_ACCESS_KEY_ID = "AKIAJRR6GNXDDKVH6GXQ"
AWS_SECRET_ACCESS_KEY = "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"

MEMCACHE = {
    'servers': ('localhost:11211',),
    'socket_timeout': 1,
}

EMAIL = {
    "server": "email-smtp.us-east-1.amazonaws.com",
    "port": 587,
    "sender": "victor.pantoja@gmail.com"
}
