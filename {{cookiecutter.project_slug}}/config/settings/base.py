import environ
from datetime import timedelta

env = environ.Env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = environ.Path(__file__) - 3
APPS_DIR = BASE_DIR.path('{{cookiecutter.project_slug}}')


# Get environment
STAGE = env('STAGE', default='local')
env.read_env(str(BASE_DIR.path('env').path(f'{STAGE.lower()}.env')))
DEBUG = env.bool('DEBUG', True)

INSTALLED_APPS = [
    'fontawesomefree',
    'admin_extended',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',
    'django_filters',
    'drf_spectacular',
    {%- if cookiecutter.use_dramatiq == "y" %}
    'django_dramatiq',
    {%- endif %}

    '{{cookiecutter.project_slug}}.core.users',
    '{{cookiecutter.project_slug}}.core.authx',
    # APPEND_NEW_APP #
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    {%- if cookiecutter.use_whitenoise == 'y' %}
    'whitenoise.middleware.WhiteNoiseMiddleware',
    {%- endif %}
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(APPS_DIR.path('templates')), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'
ROOT_URLCONF = 'config.urls'
