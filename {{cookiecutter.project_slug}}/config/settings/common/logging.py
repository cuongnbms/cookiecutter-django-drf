from ..base import env, BASE_DIR
LOG_DIR = env('LOG_DIR', default=str(BASE_DIR.path('logs')))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(module)s.%(funcName)s:%(lineno)d] %(message)s'
        },
        'simple': {
            'format': '[%(asctime)s] %(levelname)s %(module)s %(message)s'
        },
    },
    'handlers': {
        'db-file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_DIR + '/db.log',
            'formatter': 'verbose',
            'maxBytes': 10_000_000,
            'backupCount': 3,
        },
        'error-file': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_DIR + '/error.log',
            'formatter': 'verbose',
            'maxBytes': 10_000_000,
            'backupCount': 3,
        },
        'info-file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_DIR + '/info.log',
            'formatter': 'verbose',
            'maxBytes': 10_000_000,
            'backupCount': 3,
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'error-file', 'info-file'],
            'level': 'INFO',
            'propagate': True,
        },
        # 'django': {
        #     'handlers': ['console'],
        #     'level': 'INFO',
        #     'propagate': False,
        # },
        # '{{cookiecutter.project_slug}}': {
        #     'handlers': ['console'],
        #     'level': 'INFO',
        #     'propagate': False,
        # },
        # 'django.db.backends': {
        #     'handlers': ['db-file'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
    },
}
