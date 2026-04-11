REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    "DEFAULT_RENDERER_CLASSES": (
        'rest_framework.renderers.JSONRenderer',
    ),

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': (
        '{{cookiecutter.project_slug}}.apps.authx.authentication.UserJWTAuthentication',
    ),

    'EXCEPTION_HANDLER': '{{cookiecutter.project_slug}}.common.exception_handler.custom_exception_handler',

    'DEFAULT_PAGINATION_CLASS': '{{cookiecutter.project_slug}}.common.pagination.StandardPagination',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],

    'DEFAULT_THROTTLE_CLASSES': [
        '{{cookiecutter.project_slug}}.common.throttling.CloudflareScopedRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'send_email': '1/min',
    }
}
