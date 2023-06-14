DEBUG_PROPAGATE_EXCEPTIONS=True
DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3',
                        'NAME': ':memory:'}}
SITE_ID=1
SECRET_KEY='not very secret in tests'
USE_I18N=True
STATIC_URL='/static/'
ROOT_URLCONF='tests.urls'
TEMPLATE_LOADERS=(
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
MIDDLEWARE_CLASSES=(
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
INSTALLED_APPS=(
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'tests',
)
PASSWORD_HASHERS=(
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)

INSTALLED_APPS += (
    'oauth_provider',
)

INSTALLED_APPS += (
    'provider',
    'provider.oauth2',
)

ANONYMOUS_USER_ID = -1
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
)
INSTALLED_APPS += (
    'guardian',
)