import os

ENVIRONMENT = os.getenv('DJANGO_ENV', 'default')

if ENVIRONMENT == 'Development':
    DATABASES = {
        'default': {
            #database configurations for testing environment
        }
    }
elif ENVIRONMENT == 'Production':
    DATABASES = {
        'default': {
            #database configurations for testing environment
        }
    }
else:
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'root',
        'PASSWORD': 'W0rld(up',
        'HOST': '127.0.0.1',  
        'PORT': '3306',  
    }}
    