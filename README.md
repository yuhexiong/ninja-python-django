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

### In windows

```bash
$env:DEBUG="False"; python manage.py test ninjadjangoapp.tests --verbosity=0
```