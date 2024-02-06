# DjangoWeatherReminder

## Description
DjangoWeatherReminder is an application designed to provide users with current weather information retrieved from the Weatherbit API (https://www.weatherbit.io/api/weather-current). Users can access weather data through various API endpoints, including GET, POST, and UPDATE requests. Additionally, users can subscribe to receive weather updates via email for specific cities, with authorization managed through JWT tokens.

## Main Frameworks
- Django
- Django REST Framework

## API Endpoints
- `admin/`
- `api/weather-auth/login/`
- `api/weather-auth/logout/`
- `api/citiesweather/`
- `api/cities/`
- `api/subscribed/`
- `api/subscribed_delete_update/int:pk/`
- `api/token/`
- `api/token/refresh/`
- `api/token/verify/`

## Requirements
- amqp (5.0.9)
- asgiref (3.5.0)
- backports.zoneinfo (0.2.1)
- billiard (3.6.4.0)
- celery (5.2.3)
- certifi (2021.10.8)
- charset-normalizer (2.0.12)
- click (8.0.4)
- click-didyoumean (0.3.0)
- click-plugins (1.1.1)
- click-repl (0.2.0)
- Deprecated (1.2.13)
- Django (4.0.2)
- django-celery-results (2.2.0)
- djangorestframework (3.13.1)
- djangorestframework-simplejwt (5.1.0)
- gunicorn (20.1.0)
- idna (3.3)
- kombu (5.2.3)
- packaging (21.3)
- prompt-toolkit (3.0.28)
- PyJWT (2.3.0)
- pyparsing (3.0.7)
- python-dotenv (0.19.2)
- pytz (2021.3)
- redis (4.1.4)
- requests (2.27.1)
- six (1.16.0)
- sqlparse (0.4.2)
- urllib3 (1.26.8)
- vine (5.0.0)
- wcwidth (0.2.5)
- whitenoise (6.0.0)
- wrapt (1.13.3)
