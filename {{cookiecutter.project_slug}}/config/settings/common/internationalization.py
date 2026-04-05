from ..base import APPS_DIR

LANGUAGE_CODE = 'en-us'

LANGUAGES = [
    ('en', 'English'),
]

LOCALE_PATHS = [
    str(APPS_DIR.path('i18n')),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
