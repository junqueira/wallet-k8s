"""
WSGI config for apps project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apps.settings")

# from whitenoise.django import DjangoWhiteNoise
# from django.core.wsgi import get_wsgi_application


# application = get_wsgi_application()
# application = DjangoWhiteNoise(application)



from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'
application = get_wsgi_application()