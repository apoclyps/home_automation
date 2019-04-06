Home Automation
================================

A simple Django service with the goal of controlling and monitoring specific devices through the home.

> Home automation gives you access to control and monitor devices in your home from a mobile device anywhere in the world. The term may be used for isolated programmable devices, like thermostats and lighting systems, but home automation more accurately describes homes in which nearly everything — lights, appliances, electrical outlets, heating and cooling systems — are hooked up to a remotely controllable network.

### Prerequisites

- [Python](https://www.python.org/downloads/)
- [Pipenv](https://pipenv.readthedocs.io/en/latest/)

## Setup

Install required project dependencies and run the migrations to setup the SQLite Database.

```python
pipenv install
python manage.py migrate
```

## Running the Service

```
python manage.py runserver 0.0.0.0:8000
```

The Docker-based workflow makes it possible to run the service against local or remote backing services by editing configuration values and typing `docker-compose up`.

Alternatively, to run the service and it's linked services you will need to ensure the service ports are specified by using the following command:

```sh
docker-compose run --service-ports --name home_automation --rm service
```

### Maintainer

If you want to contact me, feel free to raise an issue on this repository or check out my twitter account, find me on #apoclyps.
