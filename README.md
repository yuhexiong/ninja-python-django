# Ninja

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

### migration

```bash
python manage.py migrate
```

### server

```bash
python manage.py runserver
```


server running at `http://localhost:8000`  
swagger running at `http://localhost:8000/docs`  

