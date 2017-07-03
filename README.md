# Simple Django Logger
A basic logger for Django

## Version

0.1.4

## Features

* Can log Django's request-response thread
* Can log requests made by Requests library
* Can log events
* Has four log levels: INFO, DEBUG, WARN and ERROR
* A UI to access the logs in the Django application itself
* Filters and color coded

## Dependencies

* Django 1.11
* Requests

## Installation

* Using pip

```
pip install simple_django_logger
```

## Setup

* Add in INSTALLED_APPS

```
INSTALLED_APPS = (
    ...
    'simple_django_logger',
    ...
)
```

* Add in MIDDLEWARE_CLASSES. Make sure that it is placed after all the Django middleware classes

```
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    ...
    'django_user_agents.middleware.UserAgentMiddleware',
    ...
)
```

* Add in urls.py

```
urlpatterns = [
    ...
    url(r'^logs/', include('simple_django_logger.urls', namespace='logger')),
    ...
]
```

* Access the logs by:
    - All logs: /logs/all/
    - All requests logs: /logs/requests/all/
    - All event logs: /logs/events/all/