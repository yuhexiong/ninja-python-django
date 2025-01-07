# Ninja

**(also provided Traditional Chinese version document [README-CH.md](README-CH.md).)**


Demonstration of how to use ninja to manage Django URLs and automatically generate swagger files.  

## Overview

- Language: Python v3.12
- Web FrameWork: Django v5.1.4

## ENV

copy `.env.example` as `.env`

```yaml
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432

SECRET_KEY="django-insecure-"
DEBUG=True
```

## Run

### Migration

```bash
python manage.py migrate
```

### Install Module

```bash
poetry install
```


### Run Server

```bash
python manage.py runserver
```


server running at `http://localhost:8000`  
swagger document at `http://localhost:8000/docs`  

## Test

### Linux
```bash
DEBUG=False python manage.py test authapp.tests --verbosity=0
```

### Windows

```bash
$env:DEBUG="False"; python manage.py test ninjadjangoapp.tests --verbosity=0
```



### Usage Guide

### Params  
In [app views](./ninjadjangoapp/views.py), parameters are set after the second argument of the view function. Once configured, you can directly access parameter values by their variable names in `urls`.

### Request Body  
Define the request body structure in [app schemas](./ninjadjangoapp/schemas.py), including data types, required fields, and example data. Once defined, Swagger will automatically generate the relevant documentation.  
Place the Schema in [app views](./ninjadjangoapp/views.py) as the second argument of the view function, enabling automatic parameter validation and parsing into the Schema. In the view function, you can access request parameters using `body.`.

### Response  
Define the response structure in [app schemas](./ninjadjangoapp/schemas.py) and bind the response Schema to the API endpoint in `urls`. Swagger will automatically display the response format.

### App Urls  
In [app urls](./ninjadjangoapp/urls.py), create a `Router` object and configure it using the `api_operation` method:  
- method: HTTP method (e.g., GET, POST).  
- path: API path.  
- summary: A brief description.  
- tags: Classification tags.  
- response: Specify the response Schema.  
- Specify the view function to be called.

### Project Urls  
In [project urls](./ninjadjangoproject/urls.py), create a `NinjaAPI` object and use the `add_router` method to add the `Router` from each app. This centralizes API management across all apps and displays them uniformly in Swagger.