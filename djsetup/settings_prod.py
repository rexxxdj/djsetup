DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_setup',
        'USER': 'djsetup',
        'PASSWORD': 'djsetup',
        'HOST': 'localhost',
        'PORT': '',
    }
}
