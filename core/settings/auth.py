from .common import DEBUG

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

if not DEBUG:
    AUTH_PASSWORD_VALIDATORS = [
        {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
        {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
        {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
        {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
    ]
else:
    AUTH_PASSWORD_VALIDATORS = []

AUTH_USER_MODEL = 'main.CustomUser'
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'main.auth_backend.CustomAuthBackend',
]
LOGIN_REDIRECT_URL = '/'