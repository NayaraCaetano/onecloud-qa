from .base import *

TEST = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}


# Removendo migrations
class DisableMigrations(object):
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return "notmigrations"

MIGRATION_MODULES = DisableMigrations()

# Acelerando os testes
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.CryptPasswordHasher',
)
