if IN_DOCKER:
    assert MIDDLEWARE[:1] == [
        'django.middleware.security.SecurityMiddleware',
    ]