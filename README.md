# CRUD API WITH DJANGO REST FRAMEWORK

[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

This Rest API is moddeled after https://saybravo.io/

## Requirements

- Python 3.6
- Django
- Gunicorn
- Django-heroku
- Djangorestframework

## Installation

```
	pip install -r requirements.txt
```

## Structure

In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In our case, we have one single resource, `movies`, so we will use the following URLS - `/movies/` and `/movies/<id>` for collections and elements, respectively:

| Endpoint     | HTTP Method | CRUD Method | Result           |
| ------------ | ----------- | ----------- | ---------------- |
| `v1/org`     | GET         | READ        | Get all org      |
| `v1/org/:id` | GET         | READ        | Get a single org |
| `v1/org`     | POST        | CREATE      | Create a new org |
| `v1/org/:id` | PUT         | UPDATE      | Update a org     |
| `v1/org/:id` | DELETE      | DELETE      | Delete a org     |

| Endpoint      | HTTP Method | CRUD Method | Result            |
| ------------- | ----------- | ----------- | ----------------- |
| `v1/user`     | GET         | READ        | Get all user      |
| `v1/user/:id` | GET         | READ        | Get a single user |
| `v1/user`     | POST        | CREATE      | Create a new user |
| `v1/user/:id` | PUT         | UPDATE      | Update a user     |
| `v1/user/:id` | DELETE      | DELETE      | Delete a user     |

| Endpoint          | HTTP Method | CRUD Method | Result                |
| ----------------- | ----------- | ----------- | --------------------- |
| `v1/shoutout`     | GET         | READ        | Get all shoutout      |
| `v1/shoutout/:id` | GET         | READ        | Get a single shoutout |
| `v1/shoutout`     | POST        | CREATE      | Create a new shoutout |
| `v1/shoutout/:id` | PUT         | UPDATE      | Update a shoutout     |
| `v1/shoutout/:id` | DELETE      | DELETE      | Delete a shoutout     |

## Use

We can test the API using [curl](https://curl.haxx.se/) or [httpie](https://github.com/jakubroztocil/httpie#installation). Httpie is a user friendly http client that's written in Python. Let's install that.

You can install httpie using pip:

```
pip install httpie
```

First, we have to start up Django's development server.

```
	python manage.py runserver
```

we try this:

```
	http  http://127.0.0.1:8000/v1/org/
```

we get:

```
 [
    {
        "name": "Lambda",
        "slack_org_id": "UX-12345",
        "channel_name": "General",
        "channel_id": "UX-12345",
        "access_token": "1234321342",
        "installation_date": "2019-09-23T10:09:31.031085Z",
        "bot_access_token": "3454231234531"
    },
    {
        "name": "org3",
        "slack_org_id": "wwddwdd",
        "channel_name": "wddwwddw",
        "channel_id": "dwwddww",
        "access_token": "wdwdwdw",
        "installation_date": "2019-09-23T11:49:49.858572Z",
        "bot_access_token": "wdwdwwddw"
    }
]
```

```
	http  http://127.0.0.1:8000/v1/org/
```

we get:

```
 [
    {
        "org_id": 1,
        "slack_mem_id": "123432",
        "email": "samar@samar.com",
        "name": "samar",
        "avatar": "google.com"
    },
    {
        "org_id": 1,
        "slack_mem_id": "1234232",
        "email": "Bob@bob.com",
        "name": "bob",
        "avatar": "google.com"
    }
]

```

```
	http  http://127.0.0.1:8000/v1/shoutout/
```

we get:

```
 [
    {
        "giver_id": 1,
        "receiver_id": 2,
        "message": "good boi",
        "timestamps": "2019-09-23T10:10:51.768501Z",
        "message_ts": "134554323413"
    },
    {
        "giver_id": 2,
        "receiver_id": 1,
        "message": "good job",
        "timestamps": "2019-09-23T10:11:08.339340Z",
        "message_ts": "12341"
    }
]
```
