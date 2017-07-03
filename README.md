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

* Log Django request-response thread

```
# For Django view
from simple_django_logger.utils import Logger
from simple_django_logger.response import render

class TestLogs(View):
    template_name = 'logger/logger_test.html'

    def get(self, request):
        logs = [
            Logger.log_info(request, 'Some info message. For Django render.'),
            Logger.log_debug(request, 'Some debug message. For Django render.'),
            Logger.log_warn(request, 'Some warn message. For Django render.'),
        ]

        context = {'some': 'data'}
        return render(request, self.template_name, context, logs=logs)


# For Django Rest Framework view
from simple_django_logger.utils import Logger
from simple_django_logger.response import Response

class PostAPI(APIView):

    def get(self, request, post_id):
        logs = [
            Logger.log_info(request, 'Some info message. For DRF.'),
            Logger.log_debug(request, 'Some debug message. For DRF.'),
            Logger.log_warn(request, 'Some warn message. For DRF.'),
        ]

        context = {'some': 'data'}
        return Response(
            context,
            status=status.HTTP_200_OK,
            logs=logs)
```

* Log events

```
from simple_django_logger.utils import EventLogger

EventLogger.log_debug('Some debug message', tag='tag1')
EventLogger.log_error('Some error message', tag='tag2')
EventLogger.log_info('Some info message', tag='tag3')
EventLogger.log_warn('Some warn message', tag='tag4')
```

* Log Requests calls

```
from simple_django_logger.utils import RequestLogger

response = RequestLogger.get(
    'https://jsonplaceholder.typicode.com/posts/1',
    params={'query': 'value'},
    user=request.user,
    message='Some post request message')
```

* Access the logs by:
    - All logs: /logs/all/
    - All requests logs: /logs/requests/all/
    - All event logs: /logs/events/all/